CFG_AIP_VERSION = "1.0.1"
def check_javascript_version_ctrl(cv=CFG_AIP_VERSION): #TP: added javascript version control
    """
    javascript version control (chcek version control javascript version number against version set in python)
    """
    return """<script type="text/javascript">
if (aip_version_check === null) {
	alert('version control NOT active');
} else {
	alert('version control JS : PY = *' + aip_version_check + '* : *%s*');
}
</script>""" % cv

