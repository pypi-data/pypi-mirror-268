import basc_py4chan
import threading
import os

class Scraper:
    """
    A class that represents a scraper for extracting data from 4chan threads.

    Attributes:
        QUOTES (int): Constant representing the method to scrape quotes.
        KEYWORDS (int): Constant representing the method to scrape keywords.

    Args:
        method (int): The method to use for scraping (0 for quotes, 1 for keywords).
        output (str): The path to the output file.
        limit (int, optional): The maximum number of threads to scrape. Defaults to 0 (no limit).
    """

    QUOTES = 0
    KEYWORDS = 1

    def __init__(self, method, output, limit=0):
        self.method = method
        self.output = output
        self.limit = limit
        if not os.path.exists(self.output):
            with open(self.output, 'w') as f:
                f.write('')
        self.boards = basc_py4chan.get_all_boards()
        self.links = set()

    def _board_threads(self, board):
        """
        Private method that scrapes threads from a given board.

        Args:
            board (basc_py4chan.Board): The board to scrape threads from.
        """
        thread_ids = board.get_all_thread_ids()
        for thread_id in thread_ids:
            if self.limit > 0 and self.count >= self.limit:
                break
            try:
                topic = board.get_thread(thread_id).topic
            except AttributeError:
                print('Error: ' + str(thread_id) + ' ' + board.name)
            text: str = topic.text_comment
            if self.method == 0:
                counter = 0
                lines = text.split()
                for line in lines:
                    line=line.strip()
                    if len(line) > 1:
                        if line[0] == '>' and line[1] != '>' and line[-1] != '<':
                            counter += 1
                if counter > 5:
                    self.links.add(topic.url)
                    self.count += 1
            elif self.method == 1:
                keywords = ['mfw', 'be me', 'qt3.14', '>mfw', '>be me', '>qt']
                if '>' in text:
                    for keyword in keywords:
                        if keyword in text.lower():
                            self.links.add(topic.url)
                            self.count += 1

    def scrape(self):
        """
        Scrapes threads from all boards and writes the links to the output file.
        """
        threads = []
        self.count = 0
        for board in self.boards:
            t = threading.Thread(target=self._board_threads, args=(board,))
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

        print('Writing')

        with open(self.output, 'r+') as f:
            for link in self.links:
                if link not in f.read():
                    f.write(link + '\n')

        print('Finished')

if __name__ == "__main__":
    scraper = Scraper(method=Scraper.QUOTES, output='links0.txt')
    scraper.scrape()

    scraper = Scraper(method=Scraper.KEYWORDS, output='links1.txt')
    scraper.scrape()