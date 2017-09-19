# python generator yielding training data according to settings
# TODO: implement this with a keras.utils.data_utils.Sequence() to take advantage
# fit_generator(use_multiprocessing=True)

import gensim
from numpy import random.shuffle as rand_shuffle

from person2vec import data_handler

SETTINGS = {'word_vec_source':'../person2vec/data/GoogleNews-vectors-negative300.bin'}


class TrainingDataGenerator(object):
    def __init__(self, word_vec_size, num_compare_entities):
        self.word_vectors = gensim.models.KeyedVectors.load_word2vec_format(SETTINGS['word_vec_source'], binary=True)
        self.handler = data_handler.DataHandler()
        self.word_vec_size = word_vec_size
        self.num_compare_entities = num_compare_entities
        self.num_entities = handler.entity_count()
        self.entity_dict = _create_entity_dict(handler)


    def _get_snippet_index(shuffle):
        index = self.handler.get_snippet_index()
        if shuffle:
            rand_shuffle(index)
        return index


    # reduce entities to ints to they can be loaded into keras embedding layer
    def _create_entity_x_y(name):
        entity_num = entity_dict[name]
        input_entity_nums = [entity_num]
        for i in range(0, self.num_compare_entities):
            



    # for every snippet in the db, make a training example of the number corre
    # sponding to the person along with n other random person numbers in random
    # order plus the vectorized version of the snippet. y is the position of the
    # correct person in the array of persons
    def flow_from_db(shuffle=True, batch_size=32):
        snippet_index = get_snippet_index(shuffle)
        batch = []
        for i in snippet_index:
            entity = handler.get_entities('_id':i)
            entity_x, y = self._create_entity_x_y(entity['name'])
            word_x = self._vectorize_text(i['text'])
            batch.append(([entity_x, word_x], y))
            if len(batch) >= batch_size:
                yield batch
                batch = []
