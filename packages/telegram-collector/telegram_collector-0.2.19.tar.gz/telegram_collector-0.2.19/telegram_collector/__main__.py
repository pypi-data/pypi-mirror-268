import getopt
import sys

from .__init__ import *
import configparser


def new_telegram_collector():
    tc = TelegramCollector()
    config_file = 'tg.ini'
    parser = configparser.ConfigParser()
    parser.read(config_file)

    # 参数
    tc.use_proxy = get_config(parser, 'use_proxy', True)
    if tc.use_proxy:
        tc.proxy_ip = get_config(parser, 'proxy_ip', '127.0.0.1')
        tc.proxy_port = get_config(parser, 'proxy_port', 7890)

    tc.api_id = get_config(parser, 'api_id', 0)
    tc.api_hash = get_config(parser, 'api_hash', '0')
    tc.session_name = get_config(parser, 'session_name', 'tg_session')
    tc.src_dialog_ids = get_config(parser, 'src_dialog_ids', [])
    tc.dest_dialog_ids = get_config(parser, 'dest_dialog_ids', [])
    return tc


def create_example_config_file():
    s = ('[default]\n'
         'session_name=tg_session\n'
         'api_id=0\n'
         'api_hash=0\n'
         'src_dialog_ids=0\n'
         'dest_dialog_ids=0\n'
         'use_proxy=false\n'
         ';sock5 proxy\n'
         ';proxy_ip=\n'
         ';proxy_port=\n'
         )
    with open('tg.ini', mode='w') as f:
        f.write(s)


def _get_opt():
    opts, args = getopt.getopt(sys.argv[1:], "abcp")
    for opt, _ in opts:
        return opt
    # exit
    print("-a: collect new messages\n"
          "-b: collect history messages\n"
          "-c: create an example config\n"
          "-p: print dialogs information\n")
    exit(1)


def main():
    opt = _get_opt()
    collector = new_telegram_collector()
    if opt == '-c':  # create example config
        create_example_config_file()
    elif opt == '-a':  # new message
        collector.send_new_message_src_to_dest()
    elif opt == '-b':  # history message
        collector.send_history_message_src_to_dest()
    elif opt == '-p':
        collector.print_my_dialogs()


if __name__ == '__main__':
    main()
