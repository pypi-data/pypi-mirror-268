import mysql.connector
import jieba

class CustomDictManager:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset='utf8mb4'
        )
        self.cursor = self.conn.cursor()

    def add_word(self, checkSql, sql, text, freq, tag=None):
        if self.check_word_unique(checkSql, text):
            self.cursor.execute(sql, (text, freq, tag))
            self.conn.commit()
            return True
        else:
            return False

    def check_word_unique(self, sql, text): 
        self.cursor.execute(sql, (text,))
        (count,) = self.cursor.fetchone()
        return count == 0

    def delete_word(self, sql, word_id):
        self.cursor.execute(sql, (word_id,))
        self.conn.commit()

    def update_word(self, sql, word_id, text, freq, tag=None):
        self.cursor.execute(sql, (text, freq, tag, word_id))
        self.conn.commit()

    def query_words(self, sql, page, page_size):
        offset = (page - 1) * page_size
        self.cursor.execute(sql, (page_size, offset))
        rows = self.cursor.fetchall()
        # 将查询结果转换为字典列表
        words = [{'id': row[0], 'text': row[1], 'freq': row[2], 'tag': row[3]} for row in rows]
        return words

    def load_jieba_dict(self):
        self.cursor.execute('SELECT text, freq, tag FROM custom_dict')
        for text, freq, tag in self.cursor:
            jieba.add_word(text, freq=freq, tag=tag)

    def close(self):
        self.cursor.close()
        self.conn.close()

