import os

import re


def starts_with_date(input_string):
    # 正则表达式匹配 YYYY-MM-DD 格式的日期
    pattern = r'^\d{4}-\d{2}-\d{2}'

    # 使用 re.match 检查字符串开头是否匹配该模式
    if re.match(pattern, input_string):
        return True
    else:
        return False


def generate_html_log(executing_testcase):
    # executing_testcase.logfile_full_name 是日志文件的完整路径
    # executing_testcase.full_tc_folder 是存放生成的HTML文件的目录

    # 读取日志文件内容
    with open(executing_testcase.logfile_full_name, "r") as logfile:
        execution_log = logfile.readlines()

    parts = [part for part in executing_testcase.packages.split(',') if part]
    last_part = parts[-1] if parts else ''

    testcase_name_with_package = last_part + '.' + executing_testcase.logger.name

    # 构建HTML页面
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Execution Log for TestCase</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 20px;
                padding: 0;
            }
            .container {
                background-color: white;
                border: 1px solid #ddd;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .log-entry {
                margin-bottom: 10px;
                padding: 10px;
                background-color: #f9f9f9;
                border-left: 5px solid #2196F3;
                font-size: 16px;
            }
            .error {
                border-left-color: #f44336;
            }
            .info {
                border-left-color: #4CAF50;
            }
            .timestamp {
                color: #666;
                font-size: 14px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Execution Log for TestCase: %s</h1>
    """ % testcase_name_with_package

    lines = ""
    single_line_flag = False

    # 将日志行转换为HTML元素
    for line in execution_log:
        line = line.replace("<", "&lt;").replace(">", "&gt;")
        class_name = "log-entry"
        if "ERROR" in line:
            class_name += " error"
        elif "INFO" in line:
            class_name += " info"

        if "WebDriver Action:" in line:
            action_name = line.split("'")[1]
            line = line.replace("WebDriver Action:", "<span style='color:#0066CC'>WebDriver Action:</span>")
            line = line.replace(f"'{action_name}'", f"<b style='color:#006600'>'{action_name}'</b>")
            if "args" in line:
                line = line.replace("args", "<b style='color:#333333'>args</b>")

        if "WebElement Action:" in line:
            action_name = line.split("'")[1]
            line = line.replace("WebElement Action:", "<span style='color:#0066CC'>WebElement Action:</span>")
            line = line.replace(f"'{action_name}'", f"<b style='color:#006600'>'{action_name}'</b>")
            if "args" in line:
                line = line.replace("args", "<b style='color:#333333'>args</b>")

        if "WebDriver Action:</span> <b style='color:#006600'>'save_screenshot'</b> with <b style='color:#333333'>args</b>:" in line:
            line += "<img src='" + line.split("WebDriver Action:</span> <b style='color:#006600'>'save_screenshot'</b> with <b style='color:#333333'>args</b>:")[1].strip() + "' width='100%'>"

        if "logged_requests.py" in line:
            line = line.replace("logged_requests.py", "<span style='color:#0066CC'>logged_requests.py</span>")

        if "run_test() Start" in line:
            line = line.replace("run_test() Start", "<strong style='color:#0066CC'>run_test() Start</strong>")

        if " POST Request Started" in line:
            line = line.replace(" POST Request Started", "<strong style='color:#0066CC'> POST Request Started</strong>")

        if " POST Response:" in line:
            line = line.replace(" POST Response:", "<strong style='color:#0066CC'> POST Response:</strong>")

        if "POST Request Completed" in line:
            line = line.replace("POST Request Completed", "<strong style='color:#0066CC'>POST Request Completed</strong>")

        if "GET Request Started" in line:
            line = line.replace("GET Request Started", "<strong style='color:#0066CC'>GET Request Started</strong>")

        if "GET Response" in line:
            line = line.replace("GET Response", "<strong style='color:#0066CC'>GET Response</strong>")

        if "GET Request Completed" in line:
            line = line.replace("GET Request Completed", "<strong style='color:#0066CC'>GET Request Completed</strong>")

        if "Test Execution Environment:" in line:
            line = line.replace("Test Execution Environment:", "<strong style='color:#0066CC'>Test Execution Environment:</strong>")

        if "Response [200]" in line:
            line = line.replace("Response [200]", "<strong style='color:green'>Response [200]</strong>")

        if "Response [500]" in line:
            line = line.replace("Response [500]", "<strong style='color:red'>Response [500]</strong>")


        if line == "\n":
            continue

        if starts_with_date(line):
            if single_line_flag:
                html_content += f'<div class="{class_name}"><p>{lines}</p></div>'
                lines = ""
                single_line_flag = False

            timestamp = line.split(" ")[0] + " " + line.split(" ")[1]
            html_content += f'<div class="{class_name}"><span class="timestamp">{timestamp}</span><p>{line[len(timestamp):].strip()}</p></div>'
        else:
            lines += line.replace("\n", "<br>")
            single_line_flag = True
            continue

    html_content += """
        </div>
    </body>
    </html>
    """

    # 写入HTML文件
    with open(os.path.join(executing_testcase.full_tc_folder,
                           executing_testcase.logfile_full_name.split(os.sep)[-1]).replace("log", "html"), "w") as f:
        f.write(html_content)
