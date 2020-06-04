# module for chinese text segmentation
import jieba

ch_text = "当前，世界面临食品、气候变化以及金融等多重危机，而正是这些危机更加突出了农业在发展中国家至关重要的地位"
word_list = jieba.cut(ch_text, cut_all=False)

# for i in word_list:
#     print(i)

segmented_text = "  ".join(word_list)

print(segmented_text)