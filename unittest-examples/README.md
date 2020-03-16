# �e�X�g�̗��K

### ���
- ���j�b�g�e�X�g: �֐���N���X�̒P�ʂŐU�镑���𒲂ׂ�B
- �����e�X�g�F�f�[�^�x�[�X�Ȃǂ̎��ӃR���|�[�l���g���܂߂Ď��{����B
- E2E(End-to-End)�e�X�g�F���ۂɃ��[�U�[���g�p����u���E�U�Ȃǂ̑����͕킵�ăV�X�e���S�̂�Ώۂ���B

### ���j�b�g�e�X�g
 Python�ɂ͕W�����C�u�����Ƀ��j�b�g�e�X�g���������߂̃p�b�P�[�W���p�ӂ���Ă���B
 �p�b�P�[�W���́A�uunittest�v

### �e�X�g�f�B�X�J�o��
 �@�e�X�g�͕����̃t�@�C���ɕ�������Ă���ꍇ�A�e�t�@�C���̃e�X�g���ꊇ���Ď��s����@�\�̎��B�iPython2.7�ȍ~)
 �@����̃f�B���N�g���ȉ��ɂ���S�Ẵe�X�g�����s�B
 �@Python�R�}���h��-m�I�v�V������unitest���w��B
 ������discover�T�u�R�}���h����͂��鎖���\�B��ł�-v�I�v�V����������Ǝ��s���ꂽ�e�X�g��������Ղ��Ȃ�܂��B

#### �R�}���h��F
  > $ python -m unittest discover -v
   <br> �E�E�E


   �e�X�g�f�B�X�J�o���ł̓f�B���N�g���̒�����t�@�C�����𗊂�Ƀe�X�g���L�ڂ��ꂽ�t�@�C����T���܂��B
   ���̂��߃e�X�g�L�q�����t�@�C���̖��O�ɂ͐擪�utest�v�����邱�ƁB
   �܂��A�t�@�C�����̃p�^�[���̓e�X�g�f�B�X�J�o�������s����ۂ�-p�I�v�V�������g���ĕύX���鎖���\�B

### ���b�N(�e�X�g�_�u��)
�e�X�g�Ώۂ��ʂ̃R���|�[�l���g�Ɉˑ����Ă���ƃe�X�g�������ɂ����ꍇ������܂��B���̏ꍇ�ˑ����Ă���R���|�[�l���g���֕i�ɒu�������邱�ƂŃe�X�g�������₷���Ȃ�܂��B
���́u��֕i�v�͈�ʂɁu�X�^�u�v�u���b�N�v�A���̂��u�e�X�g�_�u���v�ȂǂƌĂ΂�Ă��܂��B��Python3.3�ȍ~����W�����C�u�����Ƀ��b�N�����ׂ̃p�b�P�[�W�́uunittest.mock�v���ǉ��B

#### �R�}���h��:
 > from unittest import mock

 >  #���b�N���Ăяo���ꂽ����100��Ԃ��B<br>
 $ mock_obj = mock.Mock(return_value=100)<br>
 $ mock_obj()<br>
 100

 > #���b�N�ɕϐ���ǉ��B<br>
 $ mock_obj.name = 'Foo'<br>
 $ mock_obj.name<br>
 'Foo'
