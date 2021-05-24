import markdown
import os

def convert_all() -> None:
    '''
    Convert all markdown files in current directory to html
    '''
    for name in os.listdir():
        if name.endswith('.md'):
            with open(name, 'r', encoding='utf8') as f:
                print(name)
                text = f.read()
                html = markdown.markdown(text)

            with open(name[:-3] + '.html', 'w') as f:
                f.write(html)

def main():
    convert_all()

if __name__ == '__main__':
    main()
