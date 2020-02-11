from flask import render_template, url_for, flash,redirect, request, Blueprint
from vgginternship.extensions import  bcrypt, db
from vgginternship.models import User, Projects, Actions
from flask_login import  current_user, login_required
from vgginternship.projects.forms import projectForm, actionForm, updateActionForm

projects = Blueprint('projects', __name__)




@projects.route('/project')
@login_required
def project():
    projects = Projects.query.all()
    return render_template('project.html', projects=projects)

@projects.route('/project/new', methods = ['GET', 'POST'])
@login_required
def new_project(): 
    form = projectForm()
    if form.validate_on_submit():
        project = Projects(name= form.Projectname.data, description = form.description.data)
        db.session.add(project)
        db.session.commit()
        flash('post created', 'success')
        return redirect(url_for('projects.project'))
    return render_template('newProject.html', form = form)



@projects.route('/project/<int:project_id>')
@login_required
def projectz(project_id):
    project = Projects.query.get_or_404(project_id)
    return render_template('projectid.html', project=project)


@projects.route('/project/<int:project_id>/update', methods=['GET', 'POST'])
@login_required
def updateProject(project_id):
    project = Projects.query.get_or_404(project_id)
    form = projectForm()
    if form.validate_on_submit():
        project.name = form.Projectname.data
        project.description = form.description.data
        db.session.commit()
        flash('Updated', 'success')
        return redirect(url_for('projects.projectz', project_id=project.id))
    elif request.method == 'GET':   
        form.Projectname.data = project.name
        form.description.data = project.description
    return render_template('newProject.html', form = form)

@projects.route('/project/<int:project_id>/delete', methods=['POST', 'GET'])
@login_required
def deleteProject(project_id):
    Projects.query.filter_by(id = project_id).delete()
    db.session.commit()
    flash('Deleted', 'success')
    return redirect(url_for('projects.project'))

@projects.route('/project/<int:project_id>/addActions', methods=['POST', 'GET'])
@login_required
def addActions(project_id):
    form = actionForm()
    project = Projects.query.get_or_404(project_id)
    if form.validate_on_submit():
        action = Actions(project_id = project.id, description = form.description.data, note = form.note.data)
        db.session.add(action)
        db.session.commit()
        flash('action created', 'success')
        return redirect(url_for('projects.project'))
    return render_template('addAction.html', form = form)

@projects.route('/project/actions', methods=['POST', 'GET'])
@login_required
def allActions():
    actions = Actions.query.all()
    return render_template('allActions.html', actions=actions)

@projects.route('/project/actions/<int:action_id>')
@login_required
def allActionsId(action_id):
    action = Actions.query.get_or_404(action_id)
    return render_template('singleActionId.html', action=action)


@projects.route('/project/<int:project_id>/action')
@login_required
def specificActions(project_id):
    actions = Actions.query.filter_by(project_id = project_id)
    return render_template('specificActions.html', actions=actions)


@projects.route('/project/<int:project_id>/action/<int:action_id>')
@login_required
def specificActionsId(project_id, action_id):
    action = Actions.query.get(action_id)
    return render_template('specificActionsId.html', action=action)


@projects.route('/project/<int:project_id>/action/<int:action_id>/update', methods=['GET', 'POST'])
@login_required
def updateActions(project_id, action_id):
    action = Actions.query.get_or_404(action_id)
    form = updateActionForm()
    if form.validate_on_submit():
        action.description = form.description.data
        action.note = form.note.data
        db.session.commit()
        flash('Action updated', 'success')
        return redirect(url_for('projects.specificActionsId', project_id = action.project_id, action_id = action.id))
    elif request.method == 'GET':   
        form.description.data = action.description
        form.note.data = action.note
    return render_template('updateActions.html', form = form)

@projects.route('/project/<int:project_id>/action/<int:action_id>/delete', methods=['POST', 'GET'])
@login_required
def deleteAction(project_id, action_id):
    project = Projects.query.get_or_404(project_id)
    Actions.query.filter_by(id = action_id).delete()
    db.session.commit()
    flash('Deleted', 'success')
    return redirect(url_for('projects.specificActions', project_id = project.id))