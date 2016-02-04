import json, sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print '>>> Usage: python keyfinder.py json_filename top_level_key'
        print '>>> Example: python keyfinder.py test_feed.json place'
        sys.exit(-1)
        
    rec_cnt = key_cnt = 0
    
    with open(sys.argv[1]) as fp:
        for line in fp:
            rec_cnt += 1
            try:
                json_data = json.loads(line)
                #print json_data['user']['screen_name'], json_data['user']['location']
                if json_data[sys.argv[2]] is not None:
                    key_cnt += 1
            except:
                continue

    print 'Total Feeds -> %d Not null key count: %d' % (rec_cnt, key_cnt)
    
            
