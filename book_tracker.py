import argparse
import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name('books.json')


def load_books():
    if DATA_FILE.exists():
        try:
            with DATA_FILE.open('r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []


def save_books(books):
    with DATA_FILE.open('w', encoding='utf-8') as f:
        json.dump(books, f, ensure_ascii=False, indent=2)


def add_book(title):
    books = load_books()
    books.append(title)
    save_books(books)
    print(f'Added "{title}" to your list.')


def list_books():
    books = load_books()
    if not books:
        print('No books recorded.')
    else:
        for i, title in enumerate(books, start=1):
            print(f'{i}. {title}')


def remove_book(title):
    books = load_books()
    if title in books:
        books.remove(title)
        save_books(books)
        print(f'Removed "{title}" from your list.')
    else:
        print(f'"{title}" not found in your list.')


def parse_args():
    parser = argparse.ArgumentParser(description='Book list manager')
    sub = parser.add_subparsers(dest='command', required=True)

    add_p = sub.add_parser('add', help='Add a new book')
    add_p.add_argument('title', help='Title of the book')

    sub.add_parser('list', help='List all books')

    rm_p = sub.add_parser('remove', help='Remove a book')
    rm_p.add_argument('title', help='Title to remove')

    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == 'add':
        add_book(args.title)
    elif args.command == 'list':
        list_books()
    elif args.command == 'remove':
        remove_book(args.title)


if __name__ == '__main__':
    main()
