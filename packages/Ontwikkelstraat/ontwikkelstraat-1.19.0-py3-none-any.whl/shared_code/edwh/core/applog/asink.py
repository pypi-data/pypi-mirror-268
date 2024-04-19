import eventlet

from .sink import SyncHttpSink


class ASyncEventletHttpSink(SyncHttpSink):
    greenlets = []
    semaphore = eventlet.Semaphore()

    def commit(self):
        def locked():
            # each locked function call must use the semaphore to
            # seperate self.buffer between greenthreads.
            with self.semaphore:
                super(ASyncEventletHttpSink, self).commit()

        self.greenlets.append(eventlet.spawn(locked))

    def wait(self):
        for greenlet in self.greenlets:
            print("waiting for greenlet")
            greenlet.wait()
