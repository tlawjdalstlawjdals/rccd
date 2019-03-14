# # import matlab.engine
# #
# # # start matlab
# # eng= matlab.engine.start_matlab()
# #
# #
# # # eng.CVRMapping_GUI(nargout=0)
# #
# # eng.Realign_run_ver2(nargout=0)
# #
# #
# # from django import forms
# # from .models import Post
# #
# #
# # class PostForm(forms.ModelForm):
# #
# #     class Meta:
# #         model = Post
# #         fields = ('title', 'text', 'image', )
# # python MatlabShell.py
# #
# #
# #
# # Decay_run_ver2
#
# import matlab.engine
# engine = matlab.engine.start_matlab()
# P='..\media\BAEGSEONHUI\base\rBAEGSEONHUI.nii'
# base = 'Decay_run_ver2'
#
# getattr(engine, 'matlab.engine.shareEngine')(base, nargout=0)
# getattr(engine,'run')(base, nargout=0)


from . import MatlabShell
