class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # At each step time slice, we need to run the available task with the most
        # remaining iterations needed.
        # To do this, we can use a prio queue based on iterations left (maxheap)
        # to track what the next task should be.
        # We need to make sure only valid (not on cd) tasks enter this queue.
        # So, when we do a task, remove it from queue.
        # Replace it when time = cd expiration time
        iterations = {}
        for task in tasks:
            iterations[task] = 1 + iterations.get(task, 0)

        task_queue = [] # max heap based on remaining iterations - only store not on cd tasks
        time = 1
        for task in iterations:
            task_queue.append((iterations[task], task))

        heapq.heapify_max(task_queue)

        cooldown_expiration = {} # map time: tasks cooldown expiring at this time
        
        while True:
            # print(time, iterations, cooldown_expiration, task_queue)        
            # otherwise, add any expiring cd tasks to queue,
            # then run the first task.
            if time in cooldown_expiration:
                # print(time, "pushing", cooldown_expiration[time])
                to_push = cooldown_expiration[time]
                heapq.heappush_max(task_queue, (iterations[to_push], to_push))

            if not task_queue:
                time += 1
                continue

            running_task = heapq.heappop_max(task_queue)[1]
            # print(f"running task {running_task} at time {time}")
            iterations[running_task] -= 1
            if iterations[running_task] > 0:
                cooldown_expiration[time + n + 1] = running_task

            done = True
            for val in iterations.values():
                if val != 0:
                    done = False
            # print(time)
            if done:
                return time

            time += 1

        return time
            


