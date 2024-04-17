import argparse
from datetime import datetime, timedelta
# import difflib
import hashlib
import os
import pickle
import re
import subprocess
import sys
import time

import nltk
# from nltk.corpus import stopwords
from simplenote import Simplenote as simplenote
import toml


def fingerprint(content):
    bytes = content.encode('utf-8')
    return hashlib.sha256(bytes).hexdigest()

def update_content(filename, content, note=''):
    subdir = os.path.dirname(filename)
    if not os.path.exists(subdir):
        os.makedirs(subdir, exist_ok=True)

    current = ''
    try:
        with open(filename, 'r') as handle:
            current = handle.read()
    except FileNotFoundError:
        current = None

    if content != current:
        with open(filename, 'w') as write_handle:
            write_handle.write(content)
        if not current:
            print('++', os.path.basename(filename))
        else:
            print('<<', os.path.basename(filename))

def fix_text_problems(text):
    text = text.replace(u'\xa0', u' ')
    text = text.replace(u'\r', u'\n')
    return text

def get_note_filename(note):
    first_line = note['content'].split('\n')[0]
    for character in ('/', ':', '*', '«', '»'):
        first_line = first_line.replace(character, '')

    filename = first_line
    if len(first_line) > 60:
        # trim to 60 chars but on a word boundary
        trimmed = first_line[0:61]
        try:
            filename = trimmed[0:trimmed.rindex(' ')]
        except ValueError:
            filename = trimmed
    if len(filename) == 0:
        filename = note['key']

    return(
        filename,
        first_line[len(filename):].lstrip(),
    )

def list_active_notes():
    notes = {}
    filenames = []
    for key in database['notes']:
        note = database['notes'][key]
        if note['deleted']:
            continue
        filenames.append(note['filename'].lower())
        notes[note['filename']] = note.copy()

    for file in os.listdir(notes_dir):
        if file.startswith('.'):
            continue
        if not file.endswith('.txt'):
            continue
        if os.path.isfile(os.path.join(notes_dir, file)):
            if file.lower() not in filenames:
                notes[file] = {
                    'key': None,
                    'filename': file,
                    'version': 0,
                }
    return notes




    # # FIXME all of this is copypasta
    # body = note['content']
    # body = '\n'.join(body.split('\n')[1:]).lstrip()

    # return line

    # line = first_line(note)
    # if len(line) > 60:
    #     # line = note['key']
    #     # trim to 60 chars but on a word boundary
    #     trimmed = line[0:60]
    #     try:
    #         line = trimmed[0:trimmed.rindex(' ')]
    #     except ValueError:
    #         line = trimmed
    #     # print('** %s (%d): first line too long for filename' % (note['key'], note['version']))
    #     # print('   using', line)
    # if len(line) == 0:
    #     line = note['key']
    # return line



def update_note_data(note):
    # tags = []
    # deleted = true
    # shareURL = ""
    # publishURL = ""
    # content = "Tweaking Snow Leopard\n\n"
    # systemTags = []
    # modificationDate = 1300222845.106627
    # creationDate = 1255782266.0
    # key = "agtzaW1wbGUtbm90ZXINCxIETm90ZRiY3_cBDA"
    # version = 3
    # modifydate = 1300222845.106627
    # createdate = 1255782266.0
    # systemtags = []

    note['content'] = fix_text_problems(note['content'])
    filename, excess = get_note_filename(note)
    note['filename'] = filename
    note['body'] = (
        excess + '\n' + 
        '\n'.join(note['content'].split('\n')[1:])
    )
    if note['body'].startswith('\n\n'):
        note['body'] = note['body'][2:]
    note['fingerprint'] = fingerprint(note['body'])
    return note

def note_body(note):
    body = note['content']
    body = '\n'.join(body.split('\n')[1:])
    return body.lstrip()

# def note_title(note):
#     line = note_content(note).split('\n')[0]
#     for character in ('/', ':', '*', '«', '»'):
#         line = line.replace(character, '')
#     return line
def first_line(note):
    line = note['content'].split('\n')[0]
    for character in ('/', ':', '*', '«', '»'):
        line = line.replace(character, '')
    return line

def note_title(note):
    line = first_line(note)
    if len(line) > 60:
        # line = note['key']
        # trim to 60 chars but on a word boundary
        trimmed = line[0:60]
        try:
            line = trimmed[0:trimmed.rindex(' ')]
        except ValueError:
            line = trimmed
        # print('** %s (%d): first line too long for filename' % (note['key'], note['version']))
        # print('   using', line)
    if len(line) == 0:
        line = note['key']
    return line

def get_words_in_file(filename):
    pathname = os.path.join(notes_dir, filename)
    try:
        with open(pathname) as handle:
            content = handle.read()
        content += filename[:-4]

        words = [
            re.sub(r'[\W_]+', '', word.lower())
                for word in re.split(r'\b', content)
        ] 
        return set(
            word for word in words
                if word and len(word) < 30 and word not in stop_words
        )
    except FileNotFoundError:
        return set()

def recalculate_words_cache():
    words_cache = {}

    for note in list_active_notes():
        for word in get_words_in_file(note):
            if word not in words_cache:
                words_cache[word] = [ note, ]
            else:
                if note not in words_cache[word]:
                    words_cache[word].append(note)

    return words_cache

    # for note in database['notes']:
    #     if database['notes'][note]['deleted']:
    #         continue


    # new_cache = {}

    # def include_word(word, filename):
    #     if len(word) < 30:
    #         word = re.sub(r'[\W_]+', '', word.lower())
    #         if word and word not in stop_words:
    #             if word not in new_cache:
    #                 new_cache[word] = [filename,]
    #             else:
    #                 if filename not in new_cache[word]:
    #                     new_cache[word].append(filename)

    # for note in database['notes']:
    #     if database['notes'][note]['deleted']:
    #         continue
    #     pathname = os.path.join(notes_dir, database['notes'][note]['filename'])
    #     with open(pathname) as handle:
    #         content = handle.read()
    #     content += database['notes'][note]['filename'][:-4]
    #     for word in re.split(r'\b', content):
    #         include_word(word, database['notes'][note]['filename'])
    # return new_cache

def add_changes_to_words_cache():
    for note in list_altered_notes():
        if note['state'] == 'deleted':
            continue
        filename = note['filename']
        for word in get_words_in_file(filename):
            if word not in database['words']:
                database['words'][word] = [ filename, ]
            else:
                if note not in database['words'][word]:
                    database['words'][word].append(filename)

def perform_fetch():
    filename_to_key = {}
    for key in database['notes']:
        filename = database['notes'][key]['filename']
        filename_to_key[filename.lower()] = key

    notes, _ = sn.get_note_list(since=database['cursor'])
    # filenames = set(list_active_notes())

    # process oldest through newest, which can help
    # mitigate duplicate filenames and other issues
    for note in sorted(notes, key=lambda x: int(x['modifydate'])):
        # print(note)
        key = note['key']
        try:
            old_filename = database['notes'][key]['filename']
        except:
            old_filename = None

        # when doing a full fetch from scratch, protecting against
        # two notes with the same filename -> GOOD
        #
        # when doing an incremental fetch, 

        note = update_note_data(note)
        filename = '%s.txt' % note['filename']
        # print(old_filename, filename)

        if filename in filename_to_key and filename_to_key[filename] != key:
            index = 0
            while filename.lower() in filename_to_key:
                index += 1
                filename = '%s.%d.txt' % (note['filename'], index)
            note['filename'] = filename[:-4]

        pathname = os.path.join(notes_dir, filename)
        if old_filename and old_filename != filename:
            os.rename(
                os.path.join(notes_dir, old_filename),
                pathname,
            )
            print('  ', old_filename, '->', pathname)

        # print('**', note['filename'])

        # # DEBUG
        # if 'WhatWeLearnedAtDevFort2' in filename:
        #     print(note)

        key = note['key']
        if note['deleted']:
            if filename in filename_to_key:
                try:
                    os.remove(pathname)
                    print('--', filename)
                except FileNotFoundError:
                    # after deleting a file locally the next fetch will
                    # include the state that the file has been removed, but
                    # it has already been removed -- so, not an error
                    pass
                del filename_to_key[filename]
        else:
            filename_to_key[filename.lower()] = key
            update_content(pathname, note['body'], note)
            os.utime(pathname, (note['modifydate'], note['modifydate']))

        database['notes'][key] = note
        database['notes'][key]['filename'] = filename
        del database['notes'][key]['content']
        del database['notes'][key]['body']

    if database['cursor'] != sn.current:
        database['cursor'] = sn.current
        database['words'] = recalculate_words_cache()
        with open(os.path.join(notes_dir, 'notes.data'), 'wb') as handle:
            pickle.dump(database, handle)

def list_altered_notes():
    active_notes = list_active_notes()
    altered = []

    for key in database['notes']:
        note = database['notes'][key]
        filename = note['filename']
        pathname = os.path.join(notes_dir, filename)
        try:
            del(active_notes[filename])
        except KeyError:
            pass

        if note['deleted']:
            continue

        if os.path.exists(pathname):
            update = 0
            stamp = os.path.getmtime(pathname)
            if stamp != note['modificationDate']:
                update = 1
            with open(pathname, 'r') as handle:
                content = handle.read()
                sha = fingerprint(content)
                if sha != note['fingerprint']:
                    update = 1
            if update:
                altered.append(note.copy() | {'state': 'updated'})
        else:
            altered.append(note.copy() | {'state': 'deleted'})

    if active_notes:
        for filename in active_notes:
            pathname = os.path.join(notes_dir, filename)
            with open(pathname, 'r') as handle:
                content = filename[:-4] + "\n\n" + handle.read()
            current = os.path.getmtime(pathname)
            altered.append({
                'creationDate': current,
                'modificationDate': current,
                'content': content,
                'filename': filename,
                'state': 'new',
            })
    return altered

# FIXME test when a note is altered locally and remotely then send happens
def perform_send():
    for note in list_altered_notes():
        filename = note['filename']
        pathname = os.path.join(notes_dir, filename)
        if os.path.exists(pathname):
            stamp = os.path.getmtime(pathname)

        if note['state'] == 'new':
            with open(pathname, 'r') as handle:
                content = filename[:-4] + "\n\n" + handle.read()
            new_note, _ = sn.update_note({
                'creationDate': stamp,
                'modificationDate': stamp,
                'content': content,
            })
            print('++ note "%s" (%s)' % (filename, new_note['key']))
        elif note['state'] == 'deleted':
            print('XX', filename)
            sn.trash_note(note['key'])
        else:
            with open(pathname, 'r') as handle:
                content = handle.read()
                note['modificationDate'] = stamp
                note['modifydate'] = stamp
                note['content'] = filename[:-4] + "\n\n" + content
                print('>>', filename)
                sn.update_note(note)
    perform_fetch()

def matching_files(matches):
    matched = set(list_active_notes())

    for match in matches:
        new_matched = set()
        for word in database['words']:
            if match in word:
                new_matched = new_matched.union(set(database['words'][word]))
        matched = matched.intersection(new_matched)
    return(matched)





def edit_action(args):
    # choose preferred editor from an array of dazzling options
    editor = os.getenv(
        'NV_EDITOR',
            os.getenv('VISUAL',
                os.getenv('EDITOR', 'vi'),
    ))
    command = [editor]

    matches = matching_files(args.match)
    for match in matches:
        pathname = os.path.join(notes_dir, match)
        command.append(pathname)

    subprocess.run(command, check=True)

    # FIXME check if files were edited to see if there are changes to send

    # FIXME using database entries, not filenames
    # for match in matches:
    #     pathname = os.path.join(notes_dir, match)
    #     note = database['notes'][match]
    #     with open(pathname, 'r') as handle:
    #         content = handle.read()
    #         sha = fingerprint(content)
    #         if sha != note['fingerprint']:
    #             print(match, 'updated')
    #         else:
    #             print(match, 'same')
    #     #         update = 1
    #     # if fingerprint(database['note['body']) != 

    perform_send()

def get_note_by_filename(filename):
    for key in database['notes']:
        note = database['notes'][key]
        if note['deleted']:
            continue
        if note['filename'] == filename:
            return note
    return None

def rename_note(target, destination):
    note = get_note_by_filename(target)
    target_pathname = os.path.join(notes_dir, target)
    dest_pathname = os.path.join(notes_dir, destination)

    if not note:
        sys.exit('** Note "%s" not found.' % target)
    if not os.path.exists(target_pathname):
        sys.exit('** Note "%s" does not exist.' % target)
    if os.path.exists(dest_pathname):
        sys.exit('** Note "%s" already exists.' % destination)

    stamp = os.path.getmtime(target_pathname)
    with open(target_pathname, 'r') as handle:
        content = handle.read()
    note['modificationDate'] = stamp
    note['modifydate'] = stamp
    note['filename'] = destination
    note['content'] = destination[:-4] + "\n\n" + content

    sn.update_note(note)
    os.rename(target_pathname, dest_pathname)
    database['notes'][note['key']] = note
    print('  ', target, '->', destination)
    perform_fetch()

def all_substrings(word):
    strings = [word[i: j] for i in range(len(word))
                          for j in range(i + 1, len(word) + 1)]
    return [string for string in strings if len(string) > 1]

def list_action(args):
    for match in matching_files(args.match):
        print(match)



    # matches = set(list_notes())
    # # print('all', len(matches))

    # if args.match:
    #     for match in args.match:
    #         new_matches = set()
    #         for word in database['words']:
    #             if match in word:
    #                 # print('--', match, word)
    #                 # print(database['words'][word])
    #                 new_matches = new_matches.union(set(database['words'][word]))
    #         # print(match, new_matches)
    #         matches = matches.intersection(new_matches)
    
    # # print('now', len(matches))
    # # for match in matches:
    # #     print(match)

    # return(matches)

    # for match in matches:
    #     print(match)



    # count = 0
    # if args.match:
    #     for match in args.match:
    #         new_matches = set()
    #         # print(all_substrings(match))
    #         for word in database['words']:
    #             for string in all_substrings(match):
    #                 if string in word:
    #                     for file in database['words'][string]:
    #                         new_matches.add(file)
    #         print(new_matches)








    # # FIXME deal with tags #recipe %recipe
    # if args.match:
    #     for match in args.match:
    #         if match in database['words']:
    #             matches = matches.intersection(database['words'][match])
    #         # else:
    #             # if no exact match:
    #             # will it get worse trying to find fuzzy matches?
    #             # what if you can't get the actual match using correct words?
    #         for word in difflib.get_close_matches(match, database['words']):
    #             print('maybe try word', word)

    # for match in sorted(matches):
    #     print(match)


#     # all_notes = list_notes()

#     # for match in args.match:
#     #     print(match)
#     # sys.exit()



#     # set1 = {1, 2, 3, 4, 5}
#     # set2 = {4, 5, 6, 7, 8}

#     # common_items = set1.intersection(set2)
#     # # Alternatively, you can use the & operator:


#     # print(args)
#     # if args.match:
#     #     if args.match.startswith('#') or args.match.startswith('%'):
#     #         tagged=''

#     # # FIXME
#     # #   * get either the full list of notes or notes tagged X
#     # #   * loop over multiple match arguments further filtering
#     # #     (intersection of files matched)

#     # for note in list_notes():
#     #     if args.match:
#     #         matcher = re.compile(args.match, re.IGNORECASE)
#     #         match = re.search(matcher, note)
#     #         if match:
#     #         # if args.match in note:
#     #             print(note)
#     #     else:
#     #         print(note)

def get_note_version_caching(key, version):
    cache_file = os.path.join('/tmp', 'nv.%s.%d.pickle' % (key, version))
    if os.path.exists(cache_file):
        with open(cache_file, 'rb') as handle:
            note = pickle.load(handle)
    else:
        note, error = sn.get_note(key, version)
        if error:
            if str(note) != "HTTP Error 404: Not Found":
                sys.exit(str(note))
            note = None
    with open(cache_file, 'wb') as handle:
        pickle.dump(note, handle)
    return note

def show_recent_history(args):
    if len(args.match) != 1:
        sys.exit("Usage: nv --history 'your note file.txt'")
    show_available_history(args, 20)

def show_available_history(args, limit=0):
    if len(args.match) != 1:
        sys.exit("Usage: nv --full-history 'your note file.txt'")
    filename = args.match[0]
    note = get_note_by_filename(filename)
    if not note:
        sys.exit('** Stored note "%s" not found.' % filename)
    key = note['key']
    current = note['version']
    if not current:
        raise Stop
    if not limit:
        limit = current
    for i in range(0, limit):
        version = current - i
        if version < 1:
            break
        note_version = get_note_version_caching(key, version)
        if note_version:
            print(
                note_version['version'],
                datetime.utcfromtimestamp(int(note_version['modifydate'])),
            )

def show_note_version(args):
    if len(args.match) != 2:
        sys.exit("Usage: nv --show-version 4 'your note file.txt'")
    version = int(args.match[0])
    filename = args.match[1]
    note = get_note_by_filename(filename)
    if not note:
        sys.exit('** Stored note "%s" not found.' % filename)
    key = note['key']
    current = note['version']
    if not current:
        raise Whoops
    note_version = get_note_version_caching(key, version)
    if not note_version:
        print("""
** Stored note "%s" version %d not found.

Simplenote does not keep every version of every note forever. Notes that
have received many edits will not have all historic versions available.
Every tenth version should be, so try version %d or %d.
""" % (
                filename,
                version,
                ((version // 10) * 10 + 1),
                ((version // 10) * 10 + 11),
            ),
            file=sys.stderr
        )
        sys.exit(1)
    print(note_version['content'])

def restore_from_history(args):
    if not args.restore_version or len(args.match) != 1:
        sys.exit("Usage: nv --restore-version 4 'your note file.txt'")
    version = int(args.restore_version)
    filename = args.match[0]
    note = get_note_by_filename(filename)
    if not note:
        sys.exit('** Stored note "%s" not found.' % filename)
    key = note['key']
    current = note['version']
    if not current:
        raise Whoops
    note_version = get_note_version_caching(key, version)
    if not note_version:
        print("""
** Stored note "%s" version %d not found.

Simplenote does not keep every version of every note forever. Notes that
have received many edits will not have all historic versions available.
Every tenth version should be, so try version %d or %d.
""" % (
                filename,
                version,
                ((version // 10) * 10 + 1),
                ((version // 10) * 10 + 11),
            ),
            file=sys.stderr
        )
        sys.exit(1)
    del note_version['version']
    sn.update_note(note_version)
    perform_fetch()

def data_dump():
    print(toml.dumps(database))

def perform_watch():
    import threading
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler

    watch_interval = os.getenv('NV_WATCH_INTERVAL', 10)
    fetch_interval = os.getenv('NV_FETCH_INTERVAL', 60)
    send_timeout = timedelta(seconds=os.getenv('NV_SEND_TIMEOUT', 60))

    altered = {'list': list_altered_notes()}
    altered_lock = threading.Lock()

    class NotesHandler(FileSystemEventHandler):
        def on_any_event(self, event):
            with altered_lock:
                altered['list'] = list_altered_notes()

    def start_observer():
        event_handler = NotesHandler()
        observer = Observer()
        observer.schedule(event_handler, path=notes_dir, recursive=True)
        observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

    # Start the observer in a separate thread
    observer_thread = threading.Thread(target=start_observer)
    observer_thread.daemon = True
    observer_thread.start()

    # Main program loop
    while True:
        count=0
        while True:
            if not count % fetch_interval:
                perform_fetch()
            count = count + 1

            with altered_lock:
                send = False
                for note in altered['list']:
                    filename = note['filename']
                    pathname = os.path.join(notes_dir, filename)
                    if os.path.exists(pathname):
                        stamp = datetime.fromtimestamp(os.path.getmtime(pathname))
                        if stamp + send_timeout < datetime.now():
                            send = True
                    else:
                        send = True
                if send:
                    perform_send()

            time.sleep(watch_interval)

def main():
    parser = argparse.ArgumentParser()
    # parser.add_argument(
    #     '-h', '--help',
    #     action='store_true',
    #     help='yoyo'
    # )

    action = parser.add_argument_group('Action', 'Choose one action to perform (edit is the default)')
    group = action.add_mutually_exclusive_group()
    group.add_argument(
        '-e', '--edit',
        action = 'store_true',
        help = 'Edit all matching files',
    )
    group.add_argument(
        '-l', '--list',
        action = 'store_true',
        help = 'List all matching files',
    )
    group.add_argument(
        '-f', '--fetch',
        action = 'store_true',
        help = 'Fetch latest state from Simplenote',
    )
    group.add_argument(
        '-s', '--send',
        action = 'store_true',
        help = 'Send local changes to Simplenote',
    )
    group.add_argument(
        '-r', '--rename',
        action = 'store_true',
        help = 'Rename a note',
    )
    group.add_argument(
        '-w', '--watch',
        action = 'store_true',
        help = 'Watch forever for remote and local changes',
    )
    group.add_argument(
        '--history',
        action = 'store_true',
        help = 'List the last ten stored changes to a file',
    )
    group.add_argument(
        '--full-history',
        action = 'store_true',
        help = 'List all available stored changes to a file',
    )
    group.add_argument(
        '--show-version',
        action = 'store_true',
        help = 'Show the content of a previous version of a file',
    )
    group.add_argument(
        '--restore-version',
        type = int,
        help = 'Restore a file to a previous state',
    )
    group.add_argument(
        '--fetch-all',
        action = 'store_true',
        help = 'Pull a full copy, including as much history as is retained, from Simplenote',
    )
    group.add_argument(
        '--replay-into-repo',
        action = 'store_true',
        help = 'Using a full copy, create a git repo of your notes over time',
    )
    group.add_argument(
        '--data-dump',
        action = 'store_true',
        help = 'Dump the stored notes data in TOML format (only useful for debugging)',
    )
    parser.add_argument(
        'match',
        nargs = '*',
        help = 'word(s) to use to find matching note(s)'
    )

    args = parser.parse_args()
    # print(args)
    if True not in (
        args.edit, args.list, args.fetch, args.send, args.rename, args.watch,
        args.history, args.full_history, args.show_version,
        args.fetch_all, args.replay_into_repo, args.data_dump,
    ) and not args.restore_version:
        args.edit = True

    # print(args)
    if args.edit:
        if not args.match:
            parser.print_help()
            print("""
Editing notes requires one or more matching word(s). To edit a named file
that contains spaces, you should quote the filename: nv "file with spaces".
""")
            sys.exit(1)
        edit_action(args)
    if args.list:
        list_action(args)
    if args.fetch:
        perform_fetch()
    if args.send:
        perform_send()
    if args.watch:
        perform_watch()
    if args.rename:
        if len(args.match) != 2:
            # FIXME
            raise Stop
        else:
            rename_note(*args.match)
    if args.data_dump:
        data_dump()
    if args.history:
        show_recent_history(args)
    if args.full_history:
        show_available_history(args)
    if args.show_version:
        show_note_version(args)
    if args.restore_version:
        restore_from_history(args)

    # print()
    # print(args)

    # if args.help:
    #     parser.print_help()
    # subparsers = parser.add_subparsers(
    #     dest='action',
    # )
    # parser_fetch = subparsers.add_parser(
    #     'fetch',
    # )
    # parser_send = subparsers.add_parser(
    #     'send',
    # )
    # parser_list = subparsers.add_parser(
    #     'list',
    # )
    # parser_list.add_argument(
    #     'match',
    #     nargs = '*',
    # )
    # parser_edit = subparsers.add_parser(
    #     'edit',
    # )
    # parser_edit.add_argument(
    #     'match',
    #     nargs = '*',
    # )
    # parser_datadump = subparsers.add_parser(
    #     'datadump',
    # )

    # action = ACTIONS[args.action]
    # action(args)


# ACTIONS = {
#     'fetch': fetch_action,
#     'send': send_action,
#     'sync': sync_action,
#     'create': create_action,
#     'list': list_action,
#     'edit': edit_action,
#     'rename': rename_action,
#     # 'datadump': datadump_action,
# }

if __name__ == '__main__':
    # nltk.download('stopwords')
    stop_words = set(nltk.corpus.stopwords.words('english'))
    sn = simplenote(
        os.getenv('NV_SIMPLENOTE_USER'),
        os.getenv('NV_SIMPLENOTE_PASS')
    )
    notes_dir = os.getenv(
        'NV_NOTES_DIR',
        os.path.expanduser('~/nvnotes')
    )
    try:
        # FIXME run consistency checks
        with open(os.path.join(notes_dir, 'notes.data'), 'rb') as handle:
            database = pickle.load(handle)
        # database = toml.load(os.path.join(notes_dir, 'data.toml'))
        # with open(os.path.join(notes_dir, 'words.pickle'), 'rb') as handle:
        #     words_cache = pickle.load(handle)
    except FileNotFoundError:
        database = {'notes': {}, 'cursor': '', 'words': {}}

    add_changes_to_words_cache()
    # for note in list_altered_notes():
    #     print(note)
    main()

    # for note in list_notes():
    #     print(note)

    # data_dump()

    # database['words'] = recalculate_words_cache()
    # with open(os.path.join(notes_dir, 'notes.data'), 'wb') as handle:
    #     pickle.dump(database, handle)

    # print(get_words_in_file('an even newer file.txt'))

