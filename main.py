import sys
import argparse
import requests
import operator


def main():
    parser = get_parser()
    args = sys.argv[1:]
    parsed_args = parser.parse_args(args)
    username = parsed_args.username
    sorted_stars_info = []
    if username:
        info = get_info(username)
        if len(info.keys()) > 0:
            sorted_stars_info = sorted(
                info.items(), key=operator.itemgetter(1))
            if parsed_args.with_print:
                for cur_info in sorted_stars_info:
                    print(f'{cur_info[0]}: {cur_info[1]} stars')
        else:
            print('Not found any repositories which user was marked by star.')
    return sorted_stars_info


def get_parser():
    parser = argparse.ArgumentParser(
        description='The script for viewing stars marked by user on GitHub.')
    parser.add_argument('username', type=str,
                        help='An username.')
    parser.add_argument('-wp', '--with_print', action='store_const',
                        const=True,
                        help='print the result on console.')
    return parser


def get_info(username):
    try:
        r = requests.get(f'https://api.github.com/users/{username}/starred')
        names_and_stars = dict()
        if r.ok:
            names_and_stars = get_names_and_stars(r.json())
        else:
            print(f'Status code {r.status_code}')
        return names_and_stars
    except requests.HTTPError or requests.HTTPError as e:
        sys.stderr(f'Something gone wrong: {e}')
        sys.exit()


def get_names_and_stars(json_info):
    names_and_stars = dict()
    for info in json_info:
        if 'name' in info.keys() and 'stargazers_count' in info.keys():
            names_and_stars[info['name']] = info['stargazers_count']
    return names_and_stars


if __name__ == '__main__':
    main()
