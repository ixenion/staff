

class Event(object):

    def __init__(self):
        self.__eventhandlers = []

    def __iadd__(self, handler):
        self.__eventhandlers.append(handler)
        return self
    def __isub__(self, handlers):
        self.__eventhandlers.remove(handlers)
        return self
    def __call__(self, *args, **kwargs):
        for eventhandler in self.__eventhandlers:
            print(f'event: {eventhandler}')
            eventhandler(*args, **kwargs)


class Police(object):

    def __init__(self, phone:str):
        self.__mobile = phone

    def call_police(self):
        print(f'Police have been informed')


class Owner(object):
    
    def __init__(self, phone:str):
        self.__mobile = phone

    def call_owner(self):
        print(f'Owner has been informed')


class Alarm(object):

    def __init__(self):
        pass

    def start_alarm(self, alarm_color:str):
        print(f'Alarm started. Color {alarm_color}')


# Lock class
class Lock(object):

    def __init__(self):
        self.on_lock_broken = Event()

    def lock_broken(self):
        # This function will be executed once a lock is broken and will
        # raise an event
        self.on_lock_broken()

    # def add_subscriber_for_lock_broken_event(self, subscriber, *args, **kwargs):
    #     self.on_lock_broken += subscriber(*args, **kwargs)
    def add_subscriber_for_lock_broken_event(self, subscriber):
        self.on_lock_broken += subscriber
    
    def remove_subscriber_for_lock_broken_event(self, subscriber):
        self.on_lock_broken -= subscriber


def main():

    # Required objects
    garageLock = Lock()
    localPolice = Police('+1-543-678-12-98')
    garageOwner = Owner('+45-589-663-23-48')
    garageAlarm = Alarm()

    # Setting these objects to receive the events from lock
    garageLock.add_subscriber_for_lock_broken_event(localPolice.call_police)
    garageLock.add_subscriber_for_lock_broken_event(garageOwner.call_owner)
    garageLock.add_subscriber_for_lock_broken_event(garageAlarm.start_alarm)

    # Now the lock is broken by som burglar
    # Thus garageLock.lock_broken functioni will be called
    garageLock.lock_broken()

    # All three notification must be printed
    # as soon as Lock is broken now
    
    # Remove receiver
    garageLock.remove_subscriber_for_lock_broken_event(garageAlarm.start_alarm)

    garageLock.lock_broken()


if __name__ == '__main__':
    main()
