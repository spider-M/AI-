import pandas as pd
import logging

# -------------------------- 日志配置（核心修改）--------------------------
# 1. 获取根日志器，并清空默认处理器（避免重复输出）
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # 全局日志级别
logger.handlers.clear()

# 2. 配置【文件处理器】（写入 clean.log）
file_handler = logging.FileHandler('clean.log', mode='a', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

# 3. 配置【控制台处理器】（输出到终端）
console_handler = logging.StreamHandler()
console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)
# ----------------------------------------------------------------------

def clean_excel(input_file, output_file):
    try:
        logger.info('开始清洗数据')  # 注意：改用 logger.info，不是 logging.info
        # 解决 Excel 格式识别问题：指定 engine
        df = pd.read_excel(input_file, engine='openpyxl')
        df = df.dropna()  # 删除所有含空值的行
        df = df[df['金额'] >= 0]  # 过滤金额负数
        # 写入 Excel 也指定 engine
        df.to_excel(output_file, index=False, engine='openpyxl')
        logger.info('数据清洗完成')
    except Exception as e:
        logger.error(f'异常：{str(e)}')

if __name__ == '__main__':
    clean_excel('data.xlsx', 'result.xlsx')