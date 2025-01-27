// Datas
function soul_x(){
return battle_soul.x}

function soul_y(){
return battle_soul.y}

function soul_x_pre(){
return battle_soul.xprevious}

function soul_y_pre(){
return battle_soul.yprevious}

function soul_angle(){
return battle_soul.angle}

//Functions
function Battle_SoulGoto(xx,yy,dur,tween,ease){
Anim_Create(battle_soul,"x",tween,ease,battle_soul.x,xx-battle_soul.x,dur)
Anim_Create(battle_soul,"y",tween,ease,battle_soul.y,yy-battle_soul.y,dur)
}

function IsSoulInput(){
var inputed=0
for (var i = 0; i < 4; i++){
    if Input_IsHeld(i)
	if!inputed
	inputed=1
}
return inputed
}
function block_death(dmg){
if dmg=undefined
dmg=9999999
with(battle_soul)
if place_meeting(x,y,block)
{
	audio_play_sound(snd_hurt,1,0)
	Player_Hurt(dmg)
}
if soul_x()<board_left_pos()||soul_x()>board_right_pos()||soul_y()<board_up_pos()||soul_y()>board_down_pos()
{
	audio_play_sound(snd_hurt,1,0)
	Player_Hurt(dmg)
}
}

function Set_SoulInput(up,down,left,right){
if up=undefined
up=vk_up
if down=undefined
down=vk_down
if left=undefined
left=vk_left
if right=undefined
right=vk_right
Input_Unbind(INPUT.UP)
Input_Unbind(INPUT.DOWN)
Input_Unbind(INPUT.LEFT)
Input_Unbind(INPUT.RIGHT)
Input_Bind(INPUT.UP,INPUT_TYPE.KEYBOARD,0,up)
Input_Bind(INPUT.DOWN,INPUT_TYPE.KEYBOARD,0,down)
Input_Bind(INPUT.LEFT,INPUT_TYPE.KEYBOARD,0,left)
Input_Bind(INPUT.RIGHT,INPUT_TYPE.KEYBOARD,0,right)
}