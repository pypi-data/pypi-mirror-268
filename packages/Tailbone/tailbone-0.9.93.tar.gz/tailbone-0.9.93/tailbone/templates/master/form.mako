## -*- coding: utf-8; -*-
<%inherit file="/form.mako" />

<%def name="modify_this_page_vars()">
  ${parent.modify_this_page_vars()}
  <script type="text/javascript">

    ## declare extra data needed by form
    % for key, value in form.json_data.items():
        ${form.component_studly}Data.${key} = ${json.dumps(value)|n}
    % endfor

    % if master.deletable and instance_deletable and master.has_perm('delete') and master.delete_confirm == 'simple':

        ThisPage.methods.deleteObject = function() {
            if (confirm("Are you sure you wish to delete this ${model_title}?")) {
                this.$refs.deleteObjectForm.submit()
            }
        }

    % endif
  </script>

  ${form.render_included_templates()}

</%def>


${parent.body()}
