import sqlite3 as lite


#------------------------




def add_data(mac, info):
    try:
        conn = lite.connect("./output/chipsea_csm3510.db")
        cur = con.cursor();
        cur.execute("CREATE TABLE IF NOT EXISTS test_table(mac TEXT, info TEXT)")
        cmd = "INSERT INTO test_table(mac, info) VALUES('%s','%s');"%(mac,info)
        cur.execute(cmd)
    except Exception as e:
        print(str(e))
        raise e

if __name__ == '__main__':

    con = lite.connect('./output/chipsea_csm3510.db')
    cur = con.cursor();
    cur.execute("CREATE TABLE IF NOT EXISTS test_table(mac TEXT, info TEXT)")


    add_data("C8 B2 1E 00 00 00", "测试中")
    add_data("C8 B2 1E 00 00 01", "测试中")
    add_data("C8 B2 1E 00 00 02", "测试中")

    sel = "SELECT * FROM test_table WHERE mac='C8 B2 1E 00 00 00'"
    cur.execute(sel)
    print(sel)
    result = cur.fetchall()
    print(len(result))
    print(str(result))
    print(result)
    sel = "SELECT * FROM test_table WHERE mac='C8 B2 1E 00 00 01'"
    cur.execute(sel)
    print(sel)
    result = cur.fetchall()
    print(len(result))
    print(str(result))
    print(result)

    dele = "DELETE FROM test_table WHERE mac= 'C8 B2 1E 00 00 00'"
    rt = cur.execute(dele)
    print(rt)
    dele = "DELETE FROM test_table WHERE mac= 'C8 B2 1E 00 00 10'"
    rt = cur.execute(dele)
    print(rt)
    con.commit()
    con.close()