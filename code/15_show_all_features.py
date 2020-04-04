import re
import os
import yaml

if 'ipykernel' in sys.modules:
    CONFIG_FILE = f'../configs/config_env_jupyter.yaml'
else:
    CONFIG_FILE = f'./configs/config_env_terminal.yaml'


with open(CONFIG_FILE) as file:
    yml = yaml.load(file)
FEATURE_DIR_NAME = yml['SETTING']['FEATURE_PATH']

if __name__ == '__main__':

    files = []
    features_list = []
    for filename in os.listdir(FEATURE_DIR_NAME):
        if os.path.isfile(os.path.join(FEATURE_DIR_NAME, filename)):  # ファイルのみ取得
            files.append(filename)

    regex = re.compile(r'(.pkl)$')
    for name in files:
        if regex.search(name):
            features_list.append(name)

    features_list = [s.replace('.pkl', '') for s in features_list]
    features_list = [s.replace('_train', '') for s in features_list]
    features_list = [s.replace('_test', '') for s in features_list]
    features_list = list(set(features_list))
    features_list.sort()

    # 生成されている全特徴量の表示
    for f in features_list:
        print("," + "'" + f + "'")
