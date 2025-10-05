from office.staff import boss

boss.boss()

import office.staff.boss

office.staff.boss.boss()

import office.staff.boss as bb

bb.boss()


from office.staff.boss import *

boss()