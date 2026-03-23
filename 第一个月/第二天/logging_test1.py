import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='rpa_ai.log',
)

def run():
    try:
        logging.info('开始业务流程')
        a = 1 / 0
    except Exception as e:
        logging.error(f'执行异常:{str(e)}')
    finally:
        logging.info('流程结束')

if __name__ == '__main__':
    run()