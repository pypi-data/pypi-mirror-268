import ray
import time
import numpy as np
import scipy as sp

# DEFINITIONS
SLEEP_SECONDS_PER_TRAVEL_COORD = 1e-5
SLEEP_SECONDS_READ_FROM_S3     = 0.100
SLEEP_SECONDS_NOT_ON_SPICE     = 1.000

MAP_DIM = int(1e3)
SPICE_FIELD_PROB = 0.01
SPICE_FILE_SKEW = 0.7
S3_FILE = 2
OBJ_FILE = 1
NUM_ACTORS = 4


class BaseRivalActor:
    """
    DO NOT MODIFY

    Base class with common functionality shared across all Fedaykin and Rival Actors.
    """
    def __init__(self, payload: str):
        self.payload = payload
        self.i = np.random.randint(0, MAP_DIM - 1)
        self.j = np.random.randint(0, MAP_DIM - 1)
        self.gamestate = ray.get_actor("GameState")
        self.spice_loc_map = None
        self.spice_file_map = None
        self.order_map = None
        self.name = None

    def _set_fields(self, spice_loc_map: np.ndarray, spice_file_map: np.ndarray, order_map: dict) -> None:
        """
        This is technically not necessary but it will save a lot of people issues with a race condition.
        """
        self.spice_loc_map = spice_loc_map
        self.spice_file_map = spice_file_map
        self.order_map = order_map

    def _destroy_spice_field(self) -> bool:
        """
        DO NOT MODIFY

        (Contributes to) destroy(ing) the spice field at location: (self.i, self.j)

        Recall that order_map[(i, j)] returns the order in which your Fedaykin must
        call _destroy_spice_field() in order for the field to be fully destroyed.
        (There is no partial credit for partial destruction).

        The function will return False if the actor fails to destroy the spice field
        because either:

          A. (self.i, self.j) is not a valid spice field location, or
          B. at least one Fedaykin preceding this one in the order_map has not yet
             called _destroy_spice_field() at this location

        The function returns True if the call to destroy the spice field is successful.
        """
        # if this isn't a spice field, incur a delay and return False
        if not self.spice_loc_map[(self.i, self.j)]:
            print(f"{self.name} tried to destroy spice at {(self.i, self.j)}, but this is not a Spice location.")  # TODO: fix for h2h
            print(f"{self.name} sleeping for {SLEEP_SECONDS_NOT_ON_SPICE} seconds")
            time.sleep(SLEEP_SECONDS_NOT_ON_SPICE)
            return False

        # if file is "on S3" simulate extra delay for the network request
        if self.spice_file_map[(self.i, self.j)] == S3_FILE:
            print(f"{self.name} fetching spice field object from S3 for {(self.i, self.j)}")
            time.sleep(SLEEP_SECONDS_READ_FROM_S3)
        else:
            print(f"{self.name} fetching spice field object from OBJECT STORE for {(self.i, self.j)}")

        # get spice field object
        spice_field_ref = ray.get(self.gamestate.get_spice_field_ref.remote("southern", self.i, self.j))  # TODO: fix for h2h
        spice_field = ray.get(spice_field_ref)

        # check if spice field object can be written to
        write_order = self.order_map[(self.i, self.j)]
        try:
            write_idx = np.where(write_order == self.id)[0][0]
        except:
            print(f"{self.name} tried to destroy spice at {(self.i, self.j)} but is not a valid destroyer ({list(write_order)})")
            return False

        if np.array_equal(spice_field["writes"], write_order[:write_idx]):
            spice_field["writes"].append(self.id)
            if np.array_equal(spice_field["writes"], write_order):
                spice_field["payload"] = self.payload
                print(f"{self.name} DESTROYED SPICE FIELD AT ({(self.i, self.j)})")
            else:
                print(f"{self.name} partially destroyed spice field at ({(self.i, self.j)})")
            self.gamestate.update_spice_field_ref.remote(spice_field, self.i, self.j, "southern")  # TODO: fix for h2h
            return True

        else:
            print(f"{self.name} tried to destroy spice at {(self.i, self.j)} but current vs. destruction is: ({spice_field['writes']}) vs. ({list(write_order)})")
            return False


    def _ride_sandworm(self, new_i: int, new_j: int) -> None:
        """
        DO NOT MODIFY

        Moves your Fedaykin to the coordinates (new_i, new_j) and sleeps for the
        appropriate travel duration.
        """
        assert 0 <= new_i and new_i < MAP_DIM, f"New coord. i: {new_i} is off the map"
        assert 0 <= new_j and new_j < MAP_DIM, f"New coord. i: {new_j} is off the map"

        # calculate manhattan distance of movement
        delta_i = abs(new_i - self.i)
        delta_j = abs(new_j - self.j)
        total_dist = delta_i + delta_j

        # sleep for travel duration
        time.sleep(total_dist * SLEEP_SECONDS_PER_TRAVEL_COORD)

        # update coordinates
        self.i = new_i
        self.j = new_j


@ray.remote(num_cpus=0.1, resources={"worker3": 1e-4})
class Noop12(BaseRivalActor):
    def __init__(self, payload: str):
        super().__init__(payload)
        self.id = 12
        self.name = "Noop12"

    def start(self, spice_loc_map: np.ndarray, spice_file_map: np.ndarray, order_map: dict):
        pass

@ray.remote(num_cpus=0.1, resources={"worker4": 1e-4})
class Noop34(BaseRivalActor):
    def __init__(self, payload: str):
        super().__init__(payload)
        self.id = 34
        self.name = "Noop34"

    def start(self, spice_loc_map: np.ndarray, spice_file_map: np.ndarray, order_map: dict):
        pass


##############################################################################################
################################         Silly Goose          ################################
##############################################################################################
class BaseSillyGoose(BaseRivalActor):
    def __init__(self, payload: str):
        super().__init__(payload)

    def start(self, spice_loc_map: np.ndarray, spice_file_map: np.ndarray, order_map: dict):
        # set these state variables
        self.spice_loc_map = spice_loc_map
        self.spice_file_map = spice_file_map
        self.order_map = order_map

    def get_spice_loc_map(self):
        return self.spice_loc_map


@ray.remote(num_cpus=0.8, name="SillyGoose1", resources={"worker3": 1e-4})
class SillyGoose1(BaseSillyGoose):
    """
    SillyGoose1 is the leader. It picks which spice field to target and moves all
    other Geese to that target. Once the necessary Geese arrive, it instructs the
    Geese to destroy spice in the specified order.
    """
    def __init__(self, payload: str):
        super().__init__(payload)
        self.id = 1
        self.name = "SillyGoose1"

    def start(self, spice_loc_map: np.ndarray, spice_file_map: np.ndarray, order_map: dict):
        # set these state variables
        self.spice_loc_map = spice_loc_map
        self.spice_file_map = spice_file_map
        self.order_map = order_map

        # confirm that other actors have set variables
        all_ready = False
        while not all_ready:
            all_ready = True
            for id in [2, 3, 4]:
                goose = ray.get_actor(f"SillyGoose{id}")
                loc_map = ray.get(goose.get_spice_loc_map.remote())
                all_ready = all_ready and (loc_map is not None)

        # get spice locations and iterate over them to destroy spice
        out = np.where(spice_loc_map==1)
        for i, j in zip(out[0], out[1]):
            # move Geese that are needed to location (i,j)
            geese_ids = self.order_map[(i,j)]
            for goose_id in geese_ids:
                if goose_id != 1:
                    goose = ray.get_actor(f"SillyGoose{goose_id}")
                    goose._ride_sandworm.remote(i, j)
                else:
                    self._ride_sandworm(i, j)

            # destroy spice in synchronous fashion
            for goose_id in geese_ids:
                if goose_id != 1:
                    goose = ray.get_actor(f"SillyGoose{goose_id}")
                    ray.get(goose._destroy_spice_field.remote())
                else:
                    self._destroy_spice_field()


@ray.remote(num_cpus=0.8, name="SillyGoose2", resources={"worker3": 1e-4})
class SillyGoose2(BaseSillyGoose):
    def __init__(self, payload: str):
        super().__init__(payload)
        self.id = 2
        self.name = "SillyGoose2"

@ray.remote(num_cpus=0.8, name="SillyGoose3", resources={"worker4": 1e-4})
class SillyGoose3(BaseSillyGoose):
    def __init__(self, payload: str):
        super().__init__(payload)
        self.id = 3
        self.name = "SillyGoose3"

@ray.remote(num_cpus=0.8, name="SillyGoose4", resources={"worker4": 1e-4})
class SillyGoose4(BaseSillyGoose):
    def __init__(self, payload: str):
        super().__init__(payload)
        self.id = 4
        self.name = "SillyGoose4"


##############################################################################################
###############################         Glossu Rabban          ###############################
##############################################################################################
class BaseGlossuRabban(BaseRivalActor):
    def __init__(self, payload: str):
        super().__init__(payload)

    def start(self, spice_loc_map: np.ndarray, spice_file_map: np.ndarray, order_map: dict):
        # set these state variables
        self.spice_loc_map = spice_loc_map
        self.spice_file_map = spice_file_map
        self.order_map = order_map

    def get_spice_loc_map(self):
        return self.spice_loc_map


@ray.remote(num_cpus=0.8, name="GlossuRabban1", resources={"worker3": 1e-4})
class GlossuRabban1(BaseGlossuRabban):
    """
    GlossuRabban1 is the leader. It first filters for the subset of non-S3 spice fields.
    It then picks the closest non-S3 spice field to target and moves all other warriors to that target.
    Once the necessary warriors arrive, it instructs the warriors to destroy spice in the specified order.
    """
    def __init__(self, payload: str):
        super().__init__(payload)
        self.id = 1
        self.name = "GlossuRabban1"

    def start(self, spice_loc_map: np.ndarray, spice_file_map: np.ndarray, order_map: dict):
        # set these state variables
        self.spice_loc_map = spice_loc_map
        self.spice_file_map = spice_file_map
        self.order_map = order_map

        # confirm that other actors have set variables
        all_ready = False
        while not all_ready:
            all_ready = True
            for id in [2, 3, 4]:
                warrior = ray.get_actor(f"GlossuRabban{id}")
                loc_map = ray.get(warrior.get_spice_loc_map.remote())
                all_ready = all_ready and (loc_map is not None)

        def destroy_all_spice_of_file_type(file_type):
            # get spice locations and iterate over them to destroy spice
            spice = np.where(spice_file_map==file_type)
            for i, j in zip(spice[0], spice[1]):
                # move warriors that are needed to location (i,j)
                warrior_ids = self.order_map[(i,j)]
                for warrior_id in warrior_ids:
                    if warrior_id != 1:
                        warrior = ray.get_actor(f"GlossuRabban{warrior_id}")
                        warrior._ride_sandworm.remote(i, j)
                    else:
                        self._ride_sandworm(i, j)

                # destroy spice in synchronous fashion
                for warrior_id in warrior_ids:
                    if warrior_id != 1:
                        warrior = ray.get_actor(f"GlossuRabban{warrior_id}")
                        ray.get(warrior._destroy_spice_field.remote())
                    else:
                        self._destroy_spice_field()

        # destroy all object store spice and then all s3 spice
        destroy_all_spice_of_file_type(OBJ_FILE)
        destroy_all_spice_of_file_type(S3_FILE)


@ray.remote(num_cpus=0.8, name="GlossuRabban2", resources={"worker3": 1e-4})
class GlossuRabban2(BaseGlossuRabban):
    def __init__(self, payload: str):
        super().__init__(payload)
        self.id = 2
        self.name = "GlossuRabban2"

@ray.remote(num_cpus=0.8, name="GlossuRabban3", resources={"worker4": 1e-4})
class GlossuRabban3(BaseGlossuRabban):
    def __init__(self, payload: str):
        super().__init__(payload)
        self.id = 3
        self.name = "GlossuRabban3"

@ray.remote(num_cpus=0.8, name="GlossuRabban4", resources={"worker4": 1e-4})
class GlossuRabban4(BaseGlossuRabban):
    def __init__(self, payload: str):
        super().__init__(payload)
        self.id = 4
        self.name = "GlossuRabban4"

##############################################################################################
################################         Feyd Rautha          ################################
##############################################################################################
class BaseFeydRautha(BaseRivalActor):
    def __init__(self, payload: str):
        super().__init__(payload)
        self.id = None
        self.free = None
        self.num_singletons = {}

    def get_spice_loc_map(self):
        return self.spice_loc_map

    def is_free(self):
        return self.free

    def set_num_singletons(self, id, num_singletons):
        self.num_singletons[id] = num_singletons

    def destroy_spice_field_with_retry(self, leader):
        self.gamestate.send_message.remote(leader, self.id, {"free": False}, "rival")
        destroyed = False
        while not destroyed:
            destroyed = self._destroy_spice_field()
            time.sleep(0.0001)
        
        self.gamestate.send_message.remote(leader, self.id, {"free": True}, "rival")

    def start(self, spice_loc_map: np.ndarray, spice_file_map: np.ndarray, order_map: dict):
        # set these state variables
        self.spice_loc_map = spice_loc_map
        self.spice_file_map = spice_file_map
        self.order_map = order_map

        # construct spice arr w/this warrior's fields for finding nearest points quickly
        def get_warrior_spice_arr(file_type):
            locs, singletons = [], []
            spice = np.where(self.spice_file_map==file_type)
            idx = 0
            for i, j in zip(spice[0], spice[1]):
                warriors = self.order_map[(i, j)]
                if self.id in warriors:
                    locs.append((i, j))
                    if len(warriors) == 1:
                        singletons.append(idx)
                    idx += 1
            return np.array(locs), np.array(singletons)

        # compute location and number of singletons and update other warriors
        obj_spice_arr, obj_singletons = get_warrior_spice_arr(file_type=OBJ_FILE)
        num_singletons = len(obj_singletons)
        for id in [_id for _id in range(1, 5) if _id != self.id]:
            self.gamestate.send_message.remote(id, self.id, {"num_singletons": num_singletons}, "rival")

        # get num_singletons from every warrior to determine who leader will be (later);
        # everyone will compute the same leader
        leader, fewest_singletons = self.id, num_singletons
        for id in [_id for _id in range(1, 5) if _id != self.id]:
            num_singletons = None
            while num_singletons is None:
                msgs = ray.get(self.gamestate.get_new_messages.remote(self.id, id, "rival"))
                if len(msgs) > 0:
                    num_singletons = msgs[-1]["num_singletons"]
                time.sleep(1e-4)

            if num_singletons < fewest_singletons:
                fewest_singletons = num_singletons
                leader = id

        # destroy all the obj singletons associated with this warrior
        for i, j in obj_spice_arr[obj_singletons]:
            self._ride_sandworm(i, j)
            self._destroy_spice_field()

        # remove deleted fields from obj_spice_arr
        obj_spice_arr = np.delete(obj_spice_arr, obj_singletons, axis=0)

        # once everyone is finished, leader will run the show
        self.gamestate.send_message.remote(leader, self.id, {"free": True}, "rival")
        if self.id == leader:
            # destroy remaining obj spice
            first_pass, skipped_lst, warrior_free_states = True, [], {id: False for id in range(1, 5)}
            warrior_free_states[self.id] = True
            while first_pass or len(skipped_lst) > 0:
                first_pass = False

                for loc in obj_spice_arr:
                    i, j = loc[0], loc[1]
                    warrior_ids = self.order_map[(i,j)]

                    # if one of warrior_ids isn't free then skip
                    not_free = False
                    for warrior_id in warrior_ids:
                        msgs = ray.get(self.gamestate.get_new_messages.remote(self.id, warrior_id, "rival"))
                        if len(msgs) > 0:
                            warrior_free_states[warrior_id] = msgs[-1]["free"]
                        if not warrior_free_states[warrior_id]:
                            skipped_lst.append(loc)
                            not_free = True
                            break

                    if not_free:
                        continue

                    # otherwise, move warriors that are needed to location (i,j)
                    for warrior_id in warrior_ids:
                        if warrior_id != self.id:
                            warrior = ray.get_actor(f"FeydRautha{warrior_id}")
                            warrior._ride_sandworm.remote(i, j)
                        else:
                            self._ride_sandworm(i, j)

                    # destroy spice in asynchronous fashion
                    for warrior_id in warrior_ids:
                        if warrior_id != self.id:
                            warrior = ray.get_actor(f"FeydRautha{warrior_id}")
                            warrior.destroy_spice_field_with_retry.remote(leader=self.id)
                        else:
                            self.destroy_spice_field_with_retry(leader=self.id)

            # destroy s3 spice
            # get spice locations and iterate over them to destroy spice
            spice = np.where(spice_file_map==S3_FILE)
            for i, j in zip(spice[0], spice[1]):
                # move warriors that are needed to location (i,j)
                warrior_ids = self.order_map[(i,j)]
                for warrior_id in warrior_ids:
                    if warrior_id != self.id:
                        warrior = ray.get_actor(f"FeydRautha{warrior_id}")
                        warrior._ride_sandworm.remote(i, j)
                    else:
                        self._ride_sandworm(i, j)

                # destroy spice in synchronous fashion
                for warrior_id in warrior_ids:
                    if warrior_id != self.id:
                        warrior = ray.get_actor(f"FeydRautha{warrior_id}")
                        ray.get(warrior._destroy_spice_field.remote())
                    else:
                        self._destroy_spice_field()


@ray.remote(num_cpus=0.8, name="FeydRautha1", resources={"worker3": 1e-4})
class FeydRautha1(BaseFeydRautha):
    """
    FeydRautha computes the distance from each worker to its top-k nearest spice fields
    and coordinates which one(s) to destroy. The (k/2)-kth closest fields are selected to be destroyed,
    and if any actors which are not needed can be used to destroy one of the [k/2, k] fields in parallel
    then that is done as well.
    """
    def __init__(self, payload: str):
        super().__init__(payload)
        self.id = 1
        self.name = "FeydRautha1"
        self.k = 10

    # def start(self, spice_loc_map: np.ndarray, spice_file_map: np.ndarray, order_map: dict):
    #     # set these state variables
    #     self.spice_loc_map = spice_loc_map
    #     self.spice_file_map = spice_file_map
    #     self.order_map = order_map

    #     # construct spice arr w/this warrior's fields for finding nearest points quickly
    #     def get_warrior_spice_arr(file_type):
    #         locs, singletons = [], []
    #         spice = np.where(self.spice_file_map==file_type)
    #         idx = 0
    #         for i, j in zip(spice[0], spice[1]):
    #             warriors = self.order_map[(i, j)]
    #             if self.id in warriors:
    #                 locs.append((i, j))
    #                 if len(warriors) == 1:
    #                     singletons.append(idx)
    #                 idx += 1
    #         return np.array(locs), np.array(singletons)

    #     obj_spice_arr, obj_singletons = get_warrior_spice_arr(file_type=OBJ_FILE)

    #     # destroy all the obj singletons associated with this warrior
    #     for i, j in obj_spice_arr[obj_singletons]:
    #         self._ride_sandworm(i, j)
    #         self.destroy_block(self.id)

    #     # loop forever and destroy spice
    #     while len(obj_spice_arr) > 0:
    #         # construct spatial tree
    #         obj_spatial_tree = sp.spatial.KDTree(obj_spice_arr)

    #         # get location of each warrior
    #         other_warrior_coords = ray.get([
    #             ray.get_actor(f"FeydRautha{id}").get_location.remote()
    #             for id in [2, 3, 4]
    #         ])
    #         warrior_coords = [(self.i, self.j)] + other_warrior_coords

    #         # aggregate closest [k/2, k] spice fields for each worker
    #         close_obj_locs, close_obj_indices = [], []
    #         for i, j in warrior_coords:
    #             pt = [i, j]
    #             close_obj_loc_idxs = obj_spatial_tree.query(pt, k=self.k)[1][int(self.k/2):]
    #             close_obj_locs.extend(obj_spice_arr[close_obj_loc_idxs])
    #             close_obj_indices.extend(close_obj_loc_idxs)

    #         # filter for unique set of locations and indices
    #         close_obj_locs = np.unique(np.array(close_obj_locs), axis=0)
    #         close_obj_indices = np.unique(np.array(close_obj_indices), axis=0)

    #         # destroy all singletons first
    #         for loc in close_obj_locs:
    #             i, j = loc[0], loc[1]
    #             warriors = self.order_map[(i, j)]
    #             if len(warriors) == 1:
    #                 command_field_destroy(warriors[0])

    #         # then destroy all doubles


    #         obj_spice_arr = np.delete(obj_spice_arr, close_obj_indices, axis=0)


    #     # movement cost for each worker in order map + 1ms * num workers (obj read) [+ 100ms * num workers (s3_file read)]

    #     # 

    #     out = np.where(spice_loc_map==1)
    #     for i, j in zip(out[0], out[1]):
    #         # move warriors that are needed to location (i,j)
    #         warrior_ids = self.order_map[(i,j)]
    #         for warrior_id in warrior_ids:
    #             if warrior_id != 1:
    #                 warrior = ray.get_actor(f"FeydRautha{warrior_id}")
    #                 warrior._ride_sandworm.remote(i, j)
    #             else:
    #                 self._ride_sandworm(i, j)

    #         # destroy spice in synchronous fashion
    #         for warrior_id in warrior_ids:
    #             if warrior_id != 1:
    #                 warrior = ray.get_actor(f"FeydRautha{warrior_id}")
    #                 ray.get(warrior._destroy_spice_field.remote())
    #             else:
    #                 self._destroy_spice_field()


@ray.remote(num_cpus=0.8, name="FeydRautha2", resources={"worker3": 1e-4})
class FeydRautha2(BaseFeydRautha):
    def __init__(self, payload: str):
        super().__init__(payload)
        self.id = 2
        self.name = "FeydRautha2"

@ray.remote(num_cpus=0.8, name="FeydRautha3", resources={"worker4": 1e-4})
class FeydRautha3(BaseFeydRautha):
    def __init__(self, payload: str):
        super().__init__(payload)
        self.id = 3
        self.name = "FeydRautha3"

@ray.remote(num_cpus=0.8, name="FeydRautha4", resources={"worker4": 1e-4})
class FeydRautha4(BaseFeydRautha):
    def __init__(self, payload: str):
        super().__init__(payload)
        self.id = 4
        self.name = "FeydRautha4"
