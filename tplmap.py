#!/usr/bin/env python
from utils import cliparser
from core import checks
from core.channel import Channel
from utils.loggers import log
import traceback
import utils.config
import os

version = '0.5'

#DEBUG: python2 -m debugpy --listen 5678 --wait-for-client ./tplmap.py args...
def main():
    
    args = vars(cliparser.options)
    
    if not args.get('url'):
        cliparser.parser.error('URL is required. Run with -h for help.')
        
    # Add version
    args['version'] = version
    
    checks.check_template_injection(Channel(args))
    
if __name__ == '__main__':

    log.info(cliparser.banner % version)
    
    try:
        main()
    except (KeyboardInterrupt):
        log.info('Exiting.')
    except Exception as e:
        log.critical('Exiting: %s' % e)
        log.debug(traceback.format_exc())
        log_path = os.path.join(utils.config.base_path, 'tplmap.log')
        print('Refer to %s for more details.' % log_path)
