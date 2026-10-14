class Task:
    def __init__(self, task_id, activity_name, worker,scope,rate):
        self.task_id = task_id
        self.activity_name = activity_name
        self.worker = worker
        self.scope = scope
        self.work_done = 0
        self.rate = rate
        self.__amount = self.compute_amount()
        self.__status= "pending"

    def __str__(self):
        return(f"{self.activity_name} - {self.worker} - {self.__status}")
    
    def compute_amount(self):
        if self.work_done>0:
            self.__amount = (self.work_done)*(self.rate)

    def get_amount(self):
        return self.compute_amount()

    

    def update_work_done(self,work_done):
        self.work_done += work_done

        if self.work_done==self.scope:
            self.__status= "COMPLETE!!"
        else:
            return self.work_done

    def get_workdone(self):
        return self.work_done

    def get_status(self):
        return self.__status


