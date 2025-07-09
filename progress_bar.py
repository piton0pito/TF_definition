import sys
import time


class ProgressBar:
    def __init__(self, total, prefix='', suffix='', length=50, fill='█'):
        self.total = total
        self.prefix = prefix
        self.suffix = suffix
        self.length = length
        self.fill = fill
        self.start_time = time.time()
        self.completed = 0

    # Обновить прогресс-бар
    def update(self, increment=1):
        self.completed += increment
        if self.total > 0:
            percent = ("{0:.1f}").format(100 * (self.completed / float(self.total)))
            filled_length = int(self.length * self.completed // self.total)
            bar = self.fill * filled_length + '-' * (self.length - filled_length)
            elapsed_time = time.time() - self.start_time
            remaining_time = (elapsed_time / self.completed) * (
                        self.total - self.completed) if self.completed > 0 else 0
            sys.stdout.write(
                f'\r{self.prefix} |{bar}| {percent}% '
                f'({self.completed}/{self.total}) | '
                f'Прошло: {elapsed_time:.1f}s | '
                f'Осталось: {remaining_time:.1f}s | '
                f'{self.suffix}'
            )
            sys.stdout.flush()
        else:
            # Если total == 0, просто выводим сообщение о завершении
            sys.stdout.write(f'\r{self.prefix} |{"-" * self.length}| 0.0% (0/{self.total}) | {self.suffix}')
            sys.stdout.flush()

    # Завершить прогресс-бар
    def complete(self):
        self.update(self.total - self.completed)
