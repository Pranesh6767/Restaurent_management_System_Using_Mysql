#############################################################################
# Generated by PAGE version 5.6
#  in conjunction with Tcl version 8.6
#  Nov 20, 2020 08:24:16 PM IST  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top44 {base} {
    global vTcl
    if {$base == ""} {
        set base .top44
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m52" -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 1065x753+105+143
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1924 1055
    wm minsize $top 148 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "New Toplevel"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    menu $top.m52 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 0 
    frame $top.fra53 \
        -borderwidth 2 -relief groove -background #ff5151 -height 775 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 1113 
    vTcl:DefineAlias "$top.fra53" "Frame1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra53
    frame $site_3_0.fra54 \
        -borderwidth 2 -relief groove -background #00a800 -height 615 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 926 
    vTcl:DefineAlias "$site_3_0.fra54" "Frame2" vTcl:WidgetProc "Toplevel1" 1
    set site_4_0 $site_3_0.fra54
    frame $site_4_0.fra55 \
        -borderwidth 2 -relief groove -background #d7d700 -height 475 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 785 
    vTcl:DefineAlias "$site_4_0.fra55" "Frame3" vTcl:WidgetProc "Toplevel1" 1
    set site_5_0 $site_4_0.fra55
    frame $site_5_0.fra56 \
        -borderwidth 2 -relief groove -background #808080 -height 365 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 665 
    vTcl:DefineAlias "$site_5_0.fra56" "Frame4" vTcl:WidgetProc "Toplevel1" 1
    set site_6_0 $site_5_0.fra56
    label $site_6_0.lab57 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 22 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground #910b6e -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text {Restaurant Management Sysytem} 
    vTcl:DefineAlias "$site_6_0.lab57" "Label1" vTcl:WidgetProc "Toplevel1" 1
    label $site_6_0.lab58 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 15 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Username  :} 
    vTcl:DefineAlias "$site_6_0.lab58" "Label2_1" vTcl:WidgetProc "Toplevel1" 1
    label $site_6_0.lab59 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 15 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Password  :} 
    vTcl:DefineAlias "$site_6_0.lab59" "Label3_1" vTcl:WidgetProc "Toplevel1" 1
    entry $site_6_0.ent60 \
        -background #d8d8d8 -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 244 
    vTcl:DefineAlias "$site_6_0.ent60" "username_UI" vTcl:WidgetProc "Toplevel1" 1
    entry $site_6_0.ent61 \
        -background #d7d7d7 -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 244 
    vTcl:DefineAlias "$site_6_0.ent61" "pass_UI" vTcl:WidgetProc "Toplevel1" 1
    button $site_6_0.but62 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #ff0000 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 18 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text BILLING 
    vTcl:DefineAlias "$site_6_0.but62" "billing_UI" vTcl:WidgetProc "Toplevel1" 1
    button $site_6_0.but63 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #1515ff -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 18 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text WORKERS 
    vTcl:DefineAlias "$site_6_0.but63" "workers_UI" vTcl:WidgetProc "Toplevel1" 1
    button $site_6_0.but104 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #0000ff -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 18 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text MAINTENANCE 
    vTcl:DefineAlias "$site_6_0.but104" "maintenence_UI" vTcl:WidgetProc "Toplevel1" 1
    button $site_6_0.but105 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #ff0000 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 18 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text EXPENSES 
    vTcl:DefineAlias "$site_6_0.but105" "expenses_UI" vTcl:WidgetProc "Toplevel1" 1
    place $site_6_0.lab57 \
        -in $site_6_0 -x 0 -relx 0.075 -y 0 -rely 0.055 -width 0 \
        -relwidth 0.875 -height 0 -relheight 0.153 -anchor nw \
        -bordermode ignore 
    place $site_6_0.lab58 \
        -in $site_6_0 -x 0 -relx 0.135 -y 0 -rely 0.301 -width 0 \
        -relwidth 0.244 -height 0 -relheight 0.099 -anchor nw \
        -bordermode ignore 
    place $site_6_0.lab59 \
        -in $site_6_0 -x 0 -relx 0.135 -y 0 -rely 0.493 -width 0 \
        -relwidth 0.244 -height 0 -relheight 0.099 -anchor nw \
        -bordermode ignore 
    place $site_6_0.ent60 \
        -in $site_6_0 -x 0 -relx 0.436 -y 0 -rely 0.301 -width 244 \
        -relwidth 0 -height 34 -relheight 0 -anchor nw -bordermode ignore 
    place $site_6_0.ent61 \
        -in $site_6_0 -x 0 -relx 0.436 -y 0 -rely 0.493 -width 244 \
        -relwidth 0 -height 34 -relheight 0 -anchor nw -bordermode ignore 
    place $site_6_0.but62 \
        -in $site_6_0 -x 0 -relx 0.15 -y 0 -rely 0.658 -width 156 -relwidth 0 \
        -height 43 -relheight 0 -anchor nw -bordermode ignore 
    place $site_6_0.but63 \
        -in $site_6_0 -x 0 -relx 0.541 -y 0 -rely 0.658 -width 156 \
        -relwidth 0 -height 43 -relheight 0 -anchor nw -bordermode ignore 
    place $site_6_0.but104 \
        -in $site_6_0 -x 0 -relx 0.15 -y 0 -rely 0.849 -width 216 -relwidth 0 \
        -height 43 -relheight 0 -anchor nw -bordermode ignore 
    place $site_6_0.but105 \
        -in $site_6_0 -x 0 -relx 0.541 -y 0 -rely 0.849 -width 156 \
        -relwidth 0 -height 43 -relheight 0 -anchor nw -bordermode ignore 
    place $site_5_0.fra56 \
        -in $site_5_0 -x 0 -relx 0.076 -y 0 -rely 0.126 -width 0 \
        -relwidth 0.846 -height 0 -relheight 0.768 -anchor nw \
        -bordermode ignore 
    button $site_4_0.but106 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #408080 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 18 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {EXPORT TO EXCEL} 
    vTcl:DefineAlias "$site_4_0.but106" "exporttoexcel_UI" vTcl:WidgetProc "Toplevel1" 1
    place $site_4_0.fra55 \
        -in $site_4_0 -x 0 -relx 0.076 -y 0 -rely 0.114 -width 0 \
        -relwidth 0.848 -height 0 -relheight 0.772 -anchor nw \
        -bordermode ignore 
    place $site_4_0.but106 \
        -in $site_4_0 -x 0 -relx 0.648 -y 0 -rely 0.894 -width 286 \
        -relwidth 0 -height 53 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.fra54 \
        -in $site_3_0 -x 0 -relx 0.081 -y 0 -rely 0.103 -width 0 \
        -relwidth 0.832 -height 0 -relheight 0.794 -anchor nw \
        -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra53 \
        -in $top -x 0 -relx -0.019 -y 0 -rely -0.013 -width 0 -relwidth 1.045 \
        -height 0 -relheight 1.029 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top44 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

