from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, IPAddress


class CreateVtepIpPoolForm(FlaskForm):
    """
        ip_pool_list_start = coming from CLI argument.  Specified in the format 192.168.0.1-192.168.0.10.  multiple ranges can be specified, use comma to separate i.e 192.168.0.1-192.168.0.10,192.168.0.50-192.168.0.60
        ip_pool_mask = coming from CLI argument.  Specified in CIDR format (i.e. /24, /29, etc)
        ip_pool_gateway = coming from CLI argument.  Specified as 192.168.0.254
        number_of_hosts = count the total number of IPs across the specified range(s) and it must be at least 2x this variable.  error out if they provided fewer than this number
        ip_pool_dns = comma separated list of DNS server IPs
        ip_pool_suffix = valid domain name for dns suffix
    """
    ip_pool_list = StringField('IP Pool List ',
                           validators=[DataRequired()])

    ip_pool_mask = StringField('IP Pool Mask',
                        validators=[DataRequired()])

    ip_pool_gateway = StringField('IP Pool Gateway',
                        validators=[DataRequired(), IPAddress])

    number_of_hosts = IntegerField('Number Of Hosts',
                        validators=[DataRequired()])

    ip_pool_dns = StringField('IP Pool DNS',
                        validators=[DataRequired()])

    ip_pool_suffix = StringField('IP Pool Suffix',
                        validators=[DataRequired()])

    submit = SubmitField('Create')
