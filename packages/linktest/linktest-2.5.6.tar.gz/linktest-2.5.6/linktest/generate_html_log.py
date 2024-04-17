# -*- coding: utf-8 -*-
"""
File: generate_html_log.py
Author: Wang Lin
Date: 2023-06-05
Description:
    该文件包含了将测试用例执行日志转换为HTML格式的函数。
    主要功能包括:
    1. 读取测试用例的日志文件。
    2. 解析日志内容,提取关键信息如时间戳、日志级别等。
    3. 将日志内容转换为HTML格式,并应用样式和颜色以增强可读性。
    4. 处理特定的日志模式,如WebDriver操作、请求响应等,并对其进行高亮显示。
    5. 将转换后的HTML内容写入文件,生成测试用例执行日志的HTML报告。

Functions:
    - starts_with_date(input_string: str) -> bool
        判断字符串是否以YYYY-MM-DD格式的日期开头。

    - is_logged_requests_line(line: str) -> bool
        判断日志行是否为特定的logged_requests.py格式。

    - format_json(json_string: str) -> str
        格式化JSON字符串,使其在HTML中显示时更易读。

    - generate_html_log(executing_testcase: object) -> None
        生成测试用例执行日志的HTML报告。
        接收一个表示正在执行的测试用例的对象作为参数。
        读取测试用例的日志文件,将日志内容转换为HTML格式,并写入HTML文件。

Dependencies:
    - os: 用于文件和目录操作。
    - re: 用于正则表达式匹配。
    - json: 用于处理JSON数据。

Notes:
    - 该文件依赖于特定的测试框架和日志格式。
    - HTML样式和布局可以根据需要进行自定义和调整。
    - 生成的HTML报告文件名与原始日志文件名相同,扩展名为.html。
"""

import os
import re
import json

def starts_with_date(input_string):
    # 正则表达式匹配 YYYY-MM-DD 格式的日期
    pattern = r'^\d{4}-\d{2}-\d{2}'

    # 使用 re.match 检查字符串开头是否匹配该模式
    if re.match(pattern, input_string):
        return True
    else:
        return False


def is_logged_requests_line(line):
    pattern = r"logged_requests\.py \d+:$"
    return bool(re.search(pattern, line))


def format_json(json_string):
    try:
        parsed_json = json.loads(json_string)
        formatted_json = json.dumps(parsed_json, indent=2)
        return formatted_json.replace(" ", "&nbsp;").replace("\n", "<br>")
    except json.JSONDecodeError:
        return json_string


def generate_html_log(executing_testcase):
    # executing_testcase.logfile_full_name 是日志文件的完整路径
    # executing_testcase.full_tc_folder 是存放生成的HTML文件的目录

    case_type = "API"
    if getattr(executing_testcase, "browser", None):
        case_type = "UI"

    # 读取日志文件内容
    with open(executing_testcase.logfile_full_name, "r") as logfile:
        execution_log = logfile.readlines()

    parts = [part for part in executing_testcase.packages.split(',') if part]
    last_part = parts[-1] if parts else ''

    testcase_name_with_package = last_part + '.' + executing_testcase.logger.name

    testcase_status_info = ""
    if executing_testcase.ExecutionStatusSetByFramework == "failed":
        testcase_status_info = '<span style="padding: 8px;">Status: </span><span style="color:red; padding-right:8px;">Failed</span><button style="color: red; font-size: large; height: auto; width: auto;" onclick="scrollToTraceback()">Scroll to Traceback</button>'
    else:
        testcase_status_info = '<span style="padding: 8px;">Status: </span><span style="color:green;">Passed</span>'

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
                margin: 0;
                padding: 0;
            }
            .header {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%%;
                background-color: white;
                padding: 0px;
                box-shadow: 0 0px 0px rgba(0,0,0,0.1);
                z-index: 1;
                white-space: normal;
                word-wrap: break-word;
            }
            .container {
                margin-top: 100px;
                margin-left: 20px;
                margin-right: 20px;
                padding: 20px;
                background-color: white;
                border: 1px solid #ddd;
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
            .only-time-Log-entry {
                margin-bottom: 1px;
                margin-top: -8px;
                padding: 8px;
                background-color: #f9f9f9;
                border-left: 5px solid #2196F3;
                font-size: 12px;
            }
            .error {
                border-left-color: #f44336;
                color: #f44336;
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
        <div class="header">
            <h2 style='padding-left: 25px;'>Execution Log for TestCase: %s</h2> 
            <h3 style='padding-left: 22px;'>%s &nbsp; | &nbsp;&nbsp; CaseType: %s</h3>
        </div>
        <div class="container">
    """ % (testcase_name_with_package, testcase_status_info, case_type)

    lines = ""
    single_line_flag = False
    traceback_flag = False

    # 将日志行转换为HTML元素
    for line in execution_log:
        line = line.replace("<", "&lt;").replace(">", "&gt;")
        class_name = "log-entry"
        cls_name_only_time_Log_entry = "only-time-Log-entry"
        if "ERROR" in line:
            class_name += " error"
            cls_name_only_time_Log_entry += " error"
        elif "INFO" in line:
            class_name += " info"
            cls_name_only_time_Log_entry += " info"

        if "WebDriver Action:" in line:
            action_name = line.split("'")[1]
            line = line.replace("WebDriver Action:", "<span style='color:#0066CC'>WebDriver Action:</span>")
            line = line.replace(f"'{action_name}'", f"<b style='color:#006600; font-size: 20px;'>'{action_name}'</b>")
            if "args" in line:
                line = line.replace("args", "<b style='color:#333333'>args</b>")

        if "WebElement Action:" in line:
            action_name = line.split("'")[1]
            line = line.replace("WebElement Action:", "<span style='color:#0066CC'>WebElement Action:</span>")
            line = line.replace(f"'{action_name}'", f"<b style='color:#006600; font-size: 20px;'>'{action_name}'</b>")
            if "args" in line:
                line = line.replace("args", "<b style='color:#333333'>args</b>")

        if "WebDriver Action:</span> <b style='color:#006600; font-size: 20px;'>'save_screenshot'</b> with <b style='color:#333333'>args</b>:" in line:
            line += "<img src='" + line.split("WebDriver Action:</span> <b style='color:#006600; font-size: 20px;'>'save_screenshot'</b> with <b style='color:#333333'>args</b>:")[1].strip() + "' width='100%'>"

        # if "logged_requests.py" in line:
        #     line = line.replace("logged_requests.py", "<span style='color:#0066CC'>logged_requests.py</span>")

        if "run_test() start" in line:
            line = line.replace("run_test() start",
                                "<strong style='color:#0066CC; font-size: 20px;'>run_test() start</strong>")

        if "setup() start" in line:
            line = line.replace("setup() start",
                                "<strong style='color:#0066CC; font-size: 20px;'>setup() start</strong>")

        if "setup() end" in line:
            line = line.replace("setup() end",
                                "<strong style='color:#0066CC; font-size: 20px;'>setup() end</strong>")

        if "teardown() start" in line:
            line = line.replace("teardown() start",
                                "<strong style='color:#0066CC; font-size: 20px;'>teardown() start</strong>")

        if "teardown() end" in line:
            line = line.replace("teardown() end",
                                "<strong style='color:#0066CC; font-size: 20px;'>teardown() end</strong>")

        if "cURL Start" in line:
            line = line.replace("cURL Start",
                                "<strong style='color:#0066CC; font-size: 20px;'>cURL Start</strong>")

        if "cURL End" in line:
            line = line.replace("cURL End",
                                "<strong style='color:#0066CC; font-size: 20px;'>cURL End</strong>")

        if " POST Request Started" in line:
            line = line.replace(" POST Request Started",
                                "<strong style='color:#0066CC; font-size: 20px;'> POST Request Started</strong>")

        if " POST Response:" in line:
            line = line.replace(" POST Response:",
                                "<strong style='color:#0066CC; font-size: 20px;'> POST Response:</strong>")

        if "POST Request Completed" in line:
            line = line.replace("POST Request Completed",
                                "<strong style='color:#0066CC; font-size: 20px;'>POST Request Completed</strong>")

        if "GET Request Started" in line:
            line = line.replace("GET Request Started",
                                "<strong style='color:#0066CC; font-size: 20px;'>GET Request Started</strong>")

        if "GET Response" in line:
            line = line.replace("GET Response",
                                "<strong style='color:#0066CC; font-size: 20px;'>GET Response</strong>")

        if "GET Request Completed" in line:
            line = line.replace("GET Request Completed",
                                "<strong style='color:#0066CC; font-size: 20px;'>GET Request Completed</strong>")

        if "Test Execution Environment:" in line:
            line = line.replace("Test Execution Environment:",
                                "<strong style='color:#0066CC; font-size: 20px;'>Test Execution Environment:</strong>")

        if "Response [200]" in line:
            line = line.replace("Response [200]",
                                "<strong style='color:green; font-size: 20px;'>Response [200]</strong>")

        if "Response [201]" in line:
            line = line.replace("Response [201]",
                                "<strong style='color:green; font-size: 20px;'>Response [201]</strong>")

        if "Response [400]" in line:
            line = line.replace("Response [400]",
                                "<strong style='color:red; font-size: 20px;'>Response [400]</strong>")

        if "Response [401]" in line:
            line = line.replace("Response [401]",
                                "<strong style='color:red; font-size: 20px;'>Response [401]</strong>")

        if "Response [403]" in line:
            line = line.replace("Response [403]",
                                "<strong style='color:red; font-size: 20px;'>Response [403]</strong>")

        if "Response [404]" in line:
            line = line.replace("Response [404]",
                                "<strong style='color:red; font-size: 20px;'>Response [404]</strong>")

        if "Response [500]" in line:
            line = line.replace("Response [500]",
                                "<strong style='color:red; font-size: 20px;'>Response [500]</strong>")

        if "Response [502]" in line:
            line = line.replace("Response [502]",
                                "<strong style='color:red; font-size: 20px;'>Response [502]</strong>")

        if "Response [503]" in line:
            line = line.replace("Response [503]",
                                "<strong style='color:red; font-size: 20px;'>Response [503]</strong>")

        if "Response [504]" in line:
            line = line.replace("Response [504]",
                                "<strong style='color:red; font-size: 20px;'>Response [504]</strong>")

        if "Assertion Passed:" in line:
            line = line.replace("Assertion Passed:",
                                "<strong style='color:green; font-size: 20px;'>Assertion Passed:</strong>")

        if "Assertion Failed:" in line:
            line = line.replace("Assertion Failed:",
                                "<strong style='color:red; font-size: 20px;'>Assertion Failed:</strong>")

        if "logged_requests.py" in line:
            if "URL:" in line and "logged_requests.py" in line.split("URL:")[0]:
                line = line.replace("URL:", f"<strong style='color:#0066CC; font-size: 20px;'>URL:</strong>")
            if "JSON:" in line and "logged_requests.py" in line.split("JSON:")[0]:
                line = line.replace("JSON:",f"<strong style='color:#0066CC; font-size: 20px;'>JSON:</strong>")
            if "kwargs:" in line and "logged_requests.py" in line.split("kwargs:")[0]:
                line = line.replace("kwargs:",f"<strong style='color:#0066CC; font-size: 20px;'>kwargs:</strong>")
            if "params:" in line and "logged_requests.py" in line.split("params:")[0]:
                line = line.replace("params:", f"<strong style='color:#0066CC; font-size: 20px;'>params:</strong>")

        if line == "\n":
            continue

        if starts_with_date(line):
            if line.strip().endswith("Traceback (most recent call last):"):
                line = '<div id="linktest-traceback-section">' + line.strip() + '</div>'
                traceback_flag = True

            if single_line_flag:
                if lines.startswith("{"):
                    html_content += f'<div class="{class_name}"><pre>{format_json(lines)}</pre></div>'
                else:
                    if lines.startswith("curl "):
                        html_content += f'<div class="{class_name}"><b style="color: darkorange;">{lines}</b></div>'
                    else:
                        if traceback_flag:
                            html_content += f'<div class="log-entry error"><pre>{lines}</pre></div>'
                            traceback_flag = False
                        else:
                            html_content += f'<div class="{class_name}"><pre>{lines}</pre></div>'

                lines = ""
                single_line_flag = False

            timestamp = line.split(" ")[0] + " " + line.split(" ")[1]
            if is_logged_requests_line(line[len(timestamp):].strip()):
                html_content += f'<div class="{cls_name_only_time_Log_entry}">{line.strip()}</div>'
            else:
                html_content += f'<div class="{class_name}"><span class="timestamp">{timestamp}</span><p>{line[len(timestamp):].strip()}</p></div>'
        else:
            lines += line.replace("\n", "<br>")
            single_line_flag = True
            continue

    html_content += """
        </div>
    </body>
        <script>
            function scrollToTraceback() {
                var element = document.getElementById("linktest-traceback-section");
                element.scrollIntoView({behavior: "smooth"});
            }
        </script>
    </html>
    """

    # 写入HTML文件
    with open(os.path.join(executing_testcase.full_tc_folder,
                           executing_testcase.logfile_full_name.split(os.sep)[-1]).replace("log", "html"), "w") as f:
        f.write(html_content)
