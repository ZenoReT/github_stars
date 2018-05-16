import sys
import argparse
import requests
import operator


def main():
    parser = get_parser()
    args = sys.argv[1:]
    parsed_args = parser.parse_args(args)
    username = parsed_args.username
    are_user_repositories = parsed_args.are_user_repositories

    json_info = get_json_info(username, are_user_repositories)
    names_and_stars = get_names_and_stars(json_info)
    if len(names_and_stars.keys()) > 0:
        sorted_stars_info = sorted(
            names_and_stars.items(), key=operator.itemgetter(1), reverse=True)
        for cur_info in sorted_stars_info:
            print(f'{cur_info[0]}: {cur_info[1]} stars')
    else:
        print('Not found any repositories.')


def get_parser():
    parser = argparse.ArgumentParser(
        description='The script for viewing stars of repositories on GitHub.'
                    '\n\rYou can see information about repositories, which '
                    'user was marked by stars(default) '
                    'or about his repositories stars(use key -aur')
    parser.add_argument('username', type=str,
                        help='An username.')
    parser.add_argument('-aur', '--are_user_repositories',
                        action='store_const', const=True,
                        help='Will show user repositories stars')
    return parser


def get_json_info(username, are_user_repositories):
    try:
        stars = 'repos' if are_user_repositories else 'starred'
        r = requests.get(f'https://api.github.com/users/{username}/{stars}')
        info = []
        if r.ok:
            info = r.json()
        else:
            print(f'Status code {r.status_code}')
        return info
    except (requests.exceptions.ConnectionError, requests.HTTPError, TimeoutError) as e:
        sys.stderr.write(f'Something gone wrong: {e}')
        sys.exit(1)


def get_names_and_stars(json_info):
    names_and_stars = dict()
    for info in json_info:
        if 'name' in info.keys() and 'stargazers_count' in info.keys():
            names_and_stars[info['name']] = info['stargazers_count']
    return names_and_stars


if __name__ == '__main__':
    main()
