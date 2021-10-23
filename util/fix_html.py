import os

DIR = '../html'
EXT = 'html'

replace_dict = {
    'maze_basis.ipynb': 'maze_basis.html',
    'maze_value_iteration.ipynb': 'maze_value_iteration.html',
    'maze_policy_iteration.ipynb': 'maze_policy_iteration.html',
    '<p><span style="font-family: monospace;"></p>': '<span style="font-family: monospace;">',
    '<p>&lt;/span&gt;</p>': '</span>'
}

for file in os.listdir(DIR):
    if file.endswith(EXT):
        
        filename = os.path.join(DIR, file)
        print("Opening",filename)
		
        with open(filename, 'r') as f:
            file_str = f.read()

        for key, value in replace_dict.items():
            file_str = file_str.replace(key, value)
			
        with open(filename, 'w') as f:
            f.write(file_str)
