export BERT_BASE_DIR=/home/zhengyi_ma/ncov_sentiment/bert-models/chinese_L-12_H-768_A-12
export NCOV_DIR=/home/zhengyi_ma/ncov_sentiment/dataset_bert/
export OUTPUT_DIR=/home/zhengyi_ma/ncov_sentiment/output/

export TRAINED_CLASSIFIER=/path/to/fine/tuned/classifier

python run_classifier.py \
  --task_name=COLA \
  --do_predict=true \
  --data_dir=$NCOV_DIR \
  --vocab_file=$BERT_BASE_DIR/vocab.txt \
  --bert_config_file=$BERT_BASE_DIR/bert_config.json \
  --init_checkpoint=$BERT_BASE_DIR/bert_model.ckpt \
  --max_seq_length=128 \
  --output_dir=$OUTPUT_DIR