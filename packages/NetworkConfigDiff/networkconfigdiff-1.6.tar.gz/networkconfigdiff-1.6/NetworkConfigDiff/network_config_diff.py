import difflib

class ConfigDiff(object):

    def __init__(self, old_config, new_config):
        self.old_config = old_config
        self.new_config = new_config

    def _get_level(self,data):
        name = data.lstrip(' ')
        level =  len(data) - len(name)
        return level

    def get_true_before(self,text,target_line_number,level,fromdata_data):
        '''
        返回：{'bgp 65139': {}},{'global': {}}
        '''
        config_line = text
        line = config_line[target_line_number-1].rstrip('\n')
        conf_for_nowstrip = line.lstrip(' ')
        curr_level = self._get_level(line)
        
        if curr_level < level:
            if len(line) == len(conf_for_nowstrip):
                result = {}
                if conf_for_nowstrip == '#' or conf_for_nowstrip == '!':
                    result[fromdata_data] = {}
                    result[fromdata_data] = {}
                else:
                    result[conf_for_nowstrip] = {}
                    result[conf_for_nowstrip][fromdata_data] = {}
                return result
            else:
                # 三层，二层
                result = self.get_true_before(text,target_line_number-1,curr_level,fromdata_data) # 
                key = list(result.keys())[0]
                value = list(result[key].keys())[0]
                result[key][line] = {}
                result[key][line][value] = {}
                del result[key][value]
                return result
        elif curr_level >= level:
            for i in range(1, target_line_number):
                target_level = self._get_level(config_line[target_line_number-i])
                if target_level >= level:
                    continue
                else:
                    return self.get_true_before(text,target_line_number+1-i,level,fromdata_data) # {'bgp 65139': {}}

    def _merge_dicts(self,*dicts):
        """
        合并多个字典，其中每个字典可能包含多个嵌套级别的子字典
        """
        result = {}
        for dictionary in dicts:
            if dictionary:
                for key, value in dictionary.items():
                    if isinstance(value, dict):
                        result[key] = self._merge_dicts(result.get(key, {}), value)
                    else:
                        result[key] = value
        return result

    def collect_lines(self,diffs):
        from_all_info = {}
        to_all_info = {}
        for fromdata,todata,flag in diffs:
            if flag:
                fromdata_num,fromdata_data = fromdata
                fromdata_data = fromdata_data.replace('\0+', '')
                fromdata_data = fromdata_data.replace('\0-', '')
                fromdata_data = fromdata_data.replace('\0^', '')
                fromdata_data = fromdata_data.replace('\1', '')
                level = self._get_level(fromdata_data)
                if fromdata_data != '\n' and fromdata_num!='':
                    if level == 0:
                        from_all_info[fromdata_data] = {}
                    else:
                        output = self.get_true_before(self.old_config,fromdata_num-1,level, fromdata_data)
                        from_all_info  = self._merge_dicts(from_all_info,output)
                
                todata_num,todata_data = todata
                todata_data = todata_data.replace('\0+', '')
                todata_data = todata_data.replace('\0-', '')
                todata_data = todata_data.replace('\0^', '')
                todata_data = todata_data.replace('\1', '')
                level = self._get_level(todata_data)
                if todata_data != '\n' and todata_num != '':
                    if level == 0:
                        to_all_info[todata_data] = {}
                    else:
                        output = self.get_true_before(self.new_config,todata_num-1,level, todata_data)
                        # print(output)
                        to_all_info  = self._merge_dicts(to_all_info,output)
        return from_all_info, to_all_info

    def dict_to_conf(self,dictionary):
        keys = []

        def recursive_keys(dictionary):
            for key, value in dictionary.items():
                keys.append(key)
                if isinstance(value, dict):
                    recursive_keys(value)

        recursive_keys(dictionary)
        return '\n'.join(keys)

    def get_content_dict_and_diff(self):
        diffs = difflib._mdiff(self.old_config, self.new_config)
        from_all_info, to_all_info = self.collect_lines(diffs)
        change_old_config = self.dict_to_conf(from_all_info)
        change_new_config = self.dict_to_conf(to_all_info)
        change_new_lines = change_new_config.splitlines()
        change_old_lines = change_old_config.splitlines()
        # # 全量文字版对比
        d = difflib.Differ()
        diff = d.compare(change_old_lines, change_new_lines)
        differ = '\n'.join(list(diff))
        # print(differ)
        return differ, change_old_config, change_new_config, from_all_info, to_all_info

if __name__ == '__main__':
    text_a = open('./diff_text/192.16.102.21.txt', 'r', encoding='utf8').read().splitlines()
    text_b = open('./diff_text/change_192.16.102.21.txt', 'r', encoding='utf8').read().splitlines()
    differ, change_old_config, change_new_config, from_all_info, to_all_info = ConfigDiff(text_b, text_a).get_content_dict_and_diff()
    print(differ)
    print(change_old_config)
    print(change_new_config)
    print(from_all_info)
    print(to_all_info)
