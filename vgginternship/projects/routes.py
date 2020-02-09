from flask import render_template, url_for, flash,redirect, request, Blueprint
from VGGchallenge import  bcrypt, db
from VGGchallenge.models import User, Projects, Actions
from flask_login import  current_user, login_required
from VGGchallenge.projects.forms import projectForm, actionForm 

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
        return redirect(url_for('project'))
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

@projects.route('/project/<int:project_id>/delete', methods=['POST'])
@login_required
def deleteProject(project_id):
    project = Projects.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    flash('Updated', 'success')
    return redirect(url_for('projects.project'))

@projects.route('/project/<int:project_id>/actions', methods=['POST', 'GET'])
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

@projects.route('/project/actions')
@login_required
def allActions():
    actions = Actions.query.all()
    return render_template('allActions.html', actions=actions)

@projects.route('/project/actions/<int:action_id>')
@login_required
def allActionsId(action_id):
    action = Projects.query.get_or_404(action_id)
    return render_template('singleActionId.html', action=action)


@projects.route('/project/<int:project_id>/action')
@login_required
def specificActions(project_id):
    project = Projects.query.get_or_404(project_id)
    actions = project.actions
    return render_template('specificActions.html', actions=actions, project = project)


@projects.route('/project/<int:project_id>/action/<int:action_id>')
@login_required
def specificActionsId(project_id, action_id):
    project = Projects.query.get_or_404(project_id)
    action = project.actions.id
    return render_template('specificActionsId.html', action=action, project=project )


