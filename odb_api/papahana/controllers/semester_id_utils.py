from flask import abort

from papahana.controllers import observers_utils as obs_utils


# def confirm_associated(func):
#     def inner(sem_id):
#         print(f'decorative {sem_id}')
#         if not obs_utils.is_associated(sem_id):
#             abort(401, f"Unauthorized to access Program: {sem_id}")
#         return func(sem_id)
#     return inner

