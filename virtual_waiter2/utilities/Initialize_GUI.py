
from subprocess import Popen, PIPE, STDOUT, TimeoutExpired
from threading import Thread, Event
from queue import Queue, Empty
from tkinter import PhotoImage, Tk, Text, END, Button, Frame

class ProcessOutputReader(Thread):

    def __init__(self, queue, cmd, params=(), group=None, name=None, daemon=True):
        super().__init__(group=group, name=name, daemon=daemon)
        self._stop_request = Event()
        self.queue = queue
        self.process = Popen([(cmd,) + tuple(params)], stdout=PIPE, stderr=STDOUT, universal_newlines=True, shell=True)

    def run(self):
        for line in self.process.stdout:
            if self._stop_request.is_set():
                # if stopping was requested, terminate the process and bail out
                self.process.terminate()
                break

            self.queue.put(line)  # enqueue the line for further processing

        try:
            # give process a chance to exit gracefully
            self.process.wait(timeout=3)
        except TimeoutExpired:
            # otherwise try to terminate it forcefully
            self.process.kill()

    def stop(self):
        # request the thread to exit gracefully during its next loop iteration
        self._stop_request.set()

        # empty the queue, so the thread will be woken up
        # if it is blocking on a full queue
        while True:
            try:
                self.queue.get(block=False)
            except Empty:
                break

            self.queue.task_done()  # acknowledge line has been processed


class MyConsole(Text):

    def __init__(self, parent, queue, update_interval=50, process_lines=500):
        super().__init__(parent)
        self.queue = queue
        self.update_interval = update_interval
        self.process_lines = process_lines

        self.after(self.update_interval, self.fetch_lines)

    def fetch_lines(self):
        something_inserted = False
        subline = 0

        for _ in range(self.process_lines):
            try:
                line = self.queue.get(block=False)
                self.tag_config('background', background='light yellow', foreground='green4', font='Helvetica')
                self.tag_add('background', '1.0', END)
                self.tag_config('customer_word', background='cyan', foreground='red2', font='Helvetica')

                def search(text_widget, keyword, tag):
                    pos = '1.0'
                    while True:
                        idx = text_widget.search(keyword, pos, END)
                        if not idx:
                            break
                        pos = '{}+{}c'.format(idx, len(keyword))
                        text_widget.tag_add(tag, idx, pos)

                search(self, 'Customer said:', 'customer_word')
            except Empty:
                break

            self.insert(END, line)
            self.queue.task_done()  # acknowledge line has been processed

            # ensure scrolling the view is at most done once per interval
            something_inserted = True

        if something_inserted:
            self.see(END)

        self.after(self.update_interval, self.fetch_lines)
