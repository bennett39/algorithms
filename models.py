from collections import Counter

class Owner:
    def __init__(self):
        self.projects_owned = set()
    def own(self, project):
        self.projects_owned.add(project)
    def disown(self, project):
        self.projects_owned.remove(project)

class Worker:
    def __init__(self):
        self.projects_assigned = set()
    def join(self, project):
        self.projects_assigned.add(project)
    def leave(self, project):
        self.projects_assigned.remove(project)

class User:
    def __init__(self, name, worker=None, owner=None):
        self.name = name
        self.worker = worker
        self.owner = owner
    def owns(self):
        return self.owner.projects_owned
    def assigned(self):
        return self.worker.projects_assigned
