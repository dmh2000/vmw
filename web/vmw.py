from flask import Flask, render_template, url_for, flash, redirect
from forms import CreateVtepIpPoolForm
from create_vtep_ip_pool import create_vtep_ip_pool

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/vtep_ip_pool", methods=['GET', 'POST'])
def vtep_ip_pool():
    form = CreateVtepIpPoolForm()
    if form.validate_on_submit():
        # execute the command here
        status, xml_string = create_vtep_ip_pool(form.ip_pool_list.data,
                                                 form.ip_pool_mask.data,
                                                 form.ip_pool_gateway.data,
                                                 form.number_of_hosts.data,
                                                 form.ip_pool_dns.data,
                                                 form.ip_pool_suffix.data)
        print('STATUS:',status)
        print(xml_string)
        if status != 0:
            flash(f'Create Unsuccessful. {xml_string}', 'danger')
        else:
            flash('Created!', 'success')
            return redirect(url_for('home'))
    return render_template('vtep_ip_pool.html', title='Create VTEP IP Pool', form=form)

if __name__ == '__main__':
    app.run(debug=True)
