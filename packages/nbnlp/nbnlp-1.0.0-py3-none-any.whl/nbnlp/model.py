import os
import hanlp
from hanlp.components.ner.transformer_ner import TransformerNamedEntityRecognizer

class HanLPServer:
    def __init__(self):
        self.ner = None
        self.HanLP = None
        self.is_model_trained = False
        self.is_training = False

        # 获取当前文件的绝对路径
        current_file_path = os.path.abspath(__file__)
        # 获取当前文件所在的目录，即nbnlp目录
        project_dir = os.path.dirname(current_file_path)
        # 构建到data目录的绝对路径
        self.data_dir = os.path.join(project_dir, 'data')
        # 构建到model目录的绝对路径
        self.model_dir = os.path.join(project_dir, 'model')
        # 构建到offline目录的绝对路径
        # self.offline_dir = os.path.join(project_dir, 'offline')

    def train_model(self, epochs, finetune_path, transformer_path, fine_electra_small_zh_path):
        if self.is_training:
            return False

        self.is_training = True
        
        try:
            # 使用绝对路径
            your_training_corpus = os.path.join(self.data_dir, 'train.tsv')
            your_development_corpus = os.path.join(self.data_dir, 'test.tsv')

            save_dir = self.model_dir

            self.ner = TransformerNamedEntityRecognizer()

            # 使用绝对路径引用offline目录下的资源
            # finetune_path = os.path.join(self.offline_dir, 'MSRA_NER_ELECTRA_SMALL_ZH')
            # transformer_path = os.path.join(self.offline_dir, 'CHINESE_ELECTRA_TRANSFORMER')

            self.ner.fit(
                trn_data=your_training_corpus,
                dev_data=your_development_corpus,
                save_dir=save_dir,
                epochs=epochs,
                finetune=finetune_path,
                average_subwords=True,
                transformer=transformer_path,
            )

            # 使用绝对路径引用offline目录下的资源
            # fine_electra_small_zh_path = os.path.join(self.offline_dir, 'FINE_ELECTRA_SMALL_ZH')

            self.HanLP = hanlp.pipeline() \
                .append(hanlp.load(fine_electra_small_zh_path), output_key='tok') \
                .append(self.ner, output_key='ner')

            self.is_model_trained = True
            return True
        finally:
            self.is_training = False

    def predict(self, text):
        return self.HanLP([text])
