import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.lines as lines
from matplotlib.axes._axes import Axes
import numpy as np 

def enumerate_gates(l:list, schedule:bool=False):
    """
    遍历门序列

    两种方式进行遍历：
    一种方式直接遍历列序列，另外一种就是遍历所有的门
    当schedule为True时，则遍历所有的门序列；否则仅遍历列序列

    Args:
        l (list): 门序列，数组中每一个元素存放的是每一列的门序列
        schedule (bool, optional): 默认值是False，决定是按列遍历还是遍历所有门

    Yields:
        当schedule=True，对应的返回类型是：(int, tuple)，分别表示门序列对应的列数以及门信息
        当schedule=False，对应的返回类型是：(int, list)，分别表示门序列对应的列数以及该列所有门序列
    """
    if schedule:
        for i,gates in enumerate(l):
            for gate in gates:
                yield i,gate
    else:
        for i,gate in enumerate(l):
            yield i,gate
    return

def measured_wires(l:list, labels:list, schedule:bool=False)->dict:
    """
    确定测量门在那个比特位上，主要是确定测量门具体位置，方便后面绘制测量门

    Args:
        l (list): 门序列，数组中每一个元素存放的是每一列的门序列
        labels (list): 里面元素都是字符串，列举出每一个比特的标签
        schedule (bool, optional): 默认值是False，主要决定是按照所有门进行遍历还是按列遍历.

    Returns:
        dict: 获取一个映射关系，key是比特索引值，value是对应的列数，可以确定测量位置在哪里，方便绘图
    """
    measured = {}
    for i,gate in enumerate_gates(l, schedule=schedule):
        name,target = gate[:2]
        if isinstance(target, tuple):
            continue
        target = f"q_{target}"
        # 其主要是目的是更新测量们的起始索引，这个是方式一行有多个测量门，仅以最后一个测量门为起始索引
        # j是对应的比特位
        j = get_flipped_index(target, labels)
        if name.startswith('M'):
            measured[j] = i
    return measured

def draw_gates(ax:Axes, l:list, labels:list, gate_grid_index:list, wire_grid:np.array, plot_params:dict, measured:dict={}, schedule:bool=False):
    """
    绘制控制门
    具体逻辑如下：
    首先判断当前门的信息长度是否超过2，若是超过两个，则存在控制门（RXX、RYY、RZZ、ISWAP等都是特殊处理），则先绘制目标门，然后再绘制控制门
    若是长度不超过2，则是单门，只需要绘制目标门即可

    Args:
        ax (Axes): 绘图对象
        l (list): 门序列，数组中每一个元素存放的是每一列的门序列
        labels (list): 里面元素都是字符串，列举出每一个比特的标签
        gate_grid_index (list): 每一个比特位，对应的起始索引值（横向）
        wire_grid (np.array): 纵向位置
        plot_params (dict): 基本参数信息
        measured (dict, optional): 测量位置信息
        schedule (bool, optional): 默认值是False，主要决定是按照所有门进行遍历还是按列遍历.
    """
    for i,gate in enumerate_gates(l, schedule=schedule):
        # print(gate)
        if len(gate) > 2: # Controlled
            gate_grid_index = draw_with_controls(ax, gate, labels, gate_grid_index, wire_grid, plot_params, measured)
        else:
            if isinstance(gate[-1], tuple):
                x = max(gate_grid_index[gate[-1][0]], gate_grid_index[gate[-1][1]])
                min_index, max_index = min(gate[-1]), max(gate[-1])
                for i in range(min_index, max_index + 1):
                    gate_grid_index[i] = x + plot_params["scale"]
            else:
                target = gate[-1]
                x = gate_grid_index[target]
                gate_grid_index[target] += plot_params["scale"]
            draw_target(ax, x, gate, labels, wire_grid, plot_params)
    return

def draw_with_controls(ax:Axes, gate:tuple, labels:list, gate_grid_index:list, wire_grid:np.array, plot_params:dict, measured:dict={}):
    """
    绘制带有控制位的门

    Args:
        ax (Axes): 绘图对象
        gate (tuple): 门信息，带有门名字、目标位置以及控制位置
        labels (list): 里面元素都是字符串，列举出每一个比特的标签
        gate_grid_index (list): 每一个比特位，对应的起始索引值（横向）
        wire_grid (np.array): 纵向位置
        plot_params (dict): 基本参数信息
        measured (dict, optional): 测量位置信息

    Returns:
        list: 跟新后的每一个比特位对应的起始索引值（横向）
    """
    scale = plot_params['scale']
    name,targets = gate[:2]
    target = f"q_{targets}"
    target_index = get_flipped_index(target, labels)
    controls_index = gate[2:]
    controls = [f"q_{t}" for t in controls_index]
    control_indices = get_flipped_indices(controls, labels)
    gate_indices = control_indices + [target_index]
    min_wire = min(gate_indices)
    max_wire = max(gate_indices)
    max_col = 0
    target_contrl_index = list(controls_index) + [targets]
    min_index, max_index = min(target_contrl_index), max(target_contrl_index)
    for p in range(min_index, max_index + 1):
        if gate_grid_index[p] > max_col:
            max_col = gate_grid_index[p]
    for p in range(min_index, max_index + 1):
        gate_grid_index[p] = max_col + scale
    line(ax, max_col, max_col, wire_grid[min_wire], wire_grid[max_wire], plot_params, '#7A56D0')
    draw_target(ax, max_col, gate, labels, wire_grid, plot_params)

    for ci in control_indices:
        x = max_col
        y = wire_grid[ci]
        if name in ['SWAP']:
            swapx(ax,x,y,plot_params)
        else:
            cdot(ax,x,y,plot_params)
    return gate_grid_index

def draw_target(ax:Axes, x:float, gate:tuple, labels:list, wire_grid:np.array, plot_params:dict):
    """
    绘制目标位信息

    Args:
        ax (Axes): 绘图对象
        x (float): 横坐标位置信息
        gate (tuple): 门信息，带有门名字、目标位置以及控制位置
        labels (list): 里面元素都是字符串，列举出每一个比特的标签
        wire_grid (np.array): 纵向位置
        plot_params (dict): 基本参数信息
    """
    rectangle_delta = plot_params['rectangle_delta']
    name,target = gate[:2]
    if isinstance(target, tuple):
        # print(target)
        if 2 == len(target):
            target1 = f"q_{target[0]}"
            target2 = f'q_{target[1]}'
            target_index1 = get_flipped_index(target1, labels)
            target_index2 = get_flipped_index(target2, labels)
            y1 = wire_grid[target_index1]
            y2 = wire_grid[target_index2]
            if name in ["RXX", 'RYY', 'RZZ']:
                textstr = r'$%s_{%s}$' % (name[0], name[1:])
            elif name == 'ISWAP':
                textstr = 'iSWAP'
            else:
                textstr = name
            rectangle(ax, x - rectangle_delta, x + rectangle_delta, y1, y2, textstr, plot_params)
            return
    target = f"q_{target}"
    # x = gate_grid[target]
    target_index = get_flipped_index(target, labels)
    y = wire_grid[target_index]
    if name in ['CX','CCX']:
        oplus(ax, x, y, plot_params)
    elif name in ['CZ']:
        cdot(ax, x, y, plot_params)
    elif name in ['SWAP']:
        swapx(ax, x, y, plot_params)
    elif name in ["RX", "RY", "RZ"]:
        rotate_axis(ax, x, y, name, plot_params, box=True)
    else:
        text(ax, x, y, name, plot_params, box=True)
    return

def rectangle(ax:Axes, x1:float, x2:float, y1:float, y2:float, textstr:str, plot_params:dict):
    """
    绘制RXX, RYY, RZZ, ISWAP等用矩形来表示的门

    Args:
        ax (Axes): 绘图对象
        x1 (float): 矩形左下角横坐标
        x2 (float): 矩形右上角横坐标
        y1 (float): 矩形左下角纵坐标
        y2 (float): 矩形右上角纵坐标
        textstr (str): 在矩形中需要写入的内容
        plot_params (dict): 基本参数信息
    """
    rectangle_delta = plot_params['rectangle_delta']
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    fontsize = plot_params['fontsize']
    linewidth = plot_params['linewidth']
    y1_new = y1 - rectangle_delta
    y2_new = y2 + rectangle_delta
    width = x2 - x1
    height = y2_new - y1_new
    # rectangle = Rectangle((x1, y1_new), width, height, fc='w', ec='k', alpha=1.0, zorder=2)
    rectangle = patches.FancyBboxPatch((x1, y1_new), width, height, boxstyle='round,pad=0.09', ec='#7A56D0', fc='#E1BEE7', zorder=2, lw=linewidth)
    ax.add_patch(rectangle)
    # 开始画出对应的作用的比特
    Circle = patches.Circle
    control_radius = plot_params['control_radius']
    c = Circle((x1, y1), control_radius, ec='#7A56D0',
               fc='#7A56D0', fill=True, lw=linewidth, zorder=2)
    ax.add_patch(c)
    ax.text(x1 + rectangle_delta / 2, y1, '$1$', color='#7A56D0', ha='center', va='center', size=fontsize)
    c = Circle((x1, y2), control_radius, ec='#7A56D0',
               fc='#7A56D0', fill=True, lw=linewidth, zorder=2)
    ax.add_patch(c)
    ax.text(x1 + rectangle_delta / 2, y2, '$0$', color='#7A56D0', ha='center', va='center', size=fontsize)
    if 'iSWAP' == textstr:
        fontsize = 11.0
    ax.text(x1 + rectangle_delta, y1_new + height / 2, textstr, color='#7A56D0', ha='center', va='center', size=fontsize)
    return 

def line(ax:Axes, x1:float, x2:float, y1:float, y2:float, plot_params:dict, linecolor:str='#50C1E9'):
    """
    绘制直线

    Args:
        ax (Axes): 绘图对象
        x1 (float): 线段第一个点的横坐标
        x2 (float): 线段第二个点的横坐标
        y1 (float): 线段第一个点的纵坐标
        y2 (float): 线段第二个点的纵坐标
        plot_params (dict): 基本参数信息
        linecolor (str, optional): 线段的颜色，默认值是'#50C1E9'
    """
    Line2D = lines.Line2D
    line = Line2D((x1, x2), (y1, y2),
        color=linecolor,lw=plot_params['linewidth'])
    ax.add_line(line)

def rotate_axis(ax:Axes, x:float, y:float, textstr:str, plot_params:dict, box:bool=False):
    """
    主要是绘制RX, RY, RZ
    Args:
        ax (Axes): 绘图对象
        x (float): box中写入文字的横坐标
        y (float): box中写入文字的纵坐标
        textstr (str): 在box中需要写入的内容
        plot_params (dict): 基本参数信息
        box (bool, optional): 主要是决定是否需要重新设置bbox，默认值是False
    """
    linewidth = plot_params['linewidth']
    fontsize = plot_params['fontsize']
    box_pad = plot_params['box_pad']
    if box:
        bbox = dict(ec='#50C1E9', fc='#50C1E9', fill=True, lw=linewidth, boxstyle='round,pad=0.5')
    else:
        bbox= dict(fill=False,lw=0)
    textstr = r"$%s_%s$" % (textstr[0], textstr[1])
    targetbox = patches.FancyBboxPatch(xy=(x - box_pad, y - box_pad), height=2 * box_pad, width=2 * box_pad, ec='#50C1E9', fc='#50C1E9', fill=True, lw=linewidth, boxstyle='round,pad=0.08', zorder=2, alpha=1.0)
    ax.add_patch(targetbox)
    ax.text(x, y,textstr,color='w',ha='center',va='center',bbox=bbox,size=fontsize)
    return

def text(ax:Axes, x:float, y:float, textstr:str, plot_params:dict, textcolor:str="w", box:bool=False):
    """
    绘制一般的单门，如H, X, Y, Z等
    Args:
        ax (Axes): 绘图对象
        x (float): box中写入文字的横坐标
        y (float): box中写入文字的纵坐标
        textstr (str): 在box中需要写入的内容
        plot_params (dict): 基本参数信息
        textcolor (str, optional): 默认值是w，对应的文字颜色
        box (bool, optional): 主要是决定是否需要重新设置bbox，默认值是False
    """
    linewidth = plot_params['linewidth']
    fontsize = plot_params['fontsize']
    box_pad = plot_params['box_pad']
    # if box:
    #     bbox = dict(ec='#50C1E9', fc='#50C1E9', fill=True, lw=linewidth, boxstyle='round,pad=0.5')
    # else:
    #     bbox= dict(fill=False,lw=0)
    if textstr.endswith('DG'):
        textstr = r'$%s^\dagger$' % textstr[0]
    targetbox = patches.FancyBboxPatch(xy=(x - box_pad, y - box_pad), height=2 * box_pad, width=2 * box_pad, ec='#50C1E9', fc='#50C1E9', fill=True, lw=linewidth, boxstyle='round,pad=0.08', zorder=2)
    ax.add_patch(targetbox)
    ax.text(x, y, textstr, color=textcolor, ha='center', va='center', size=fontsize)
    return

def oplus(ax:Axes, x:float, y:float, plot_params:dict):
    """
    绘制CX和CCX这两个门，主要是解决直和那个符号
    Args:
        ax (Axes): 绘图对象
        x (float): 对应的圆心横坐标
        y (float): 对应的圆心纵坐标
        plot_params (dict): 基本参数信息
    """
    Circle = patches.Circle
    not_radius = plot_params['not_radius']
    linewidth = plot_params['linewidth']
    c = Circle((x, y), not_radius, ec='#7A56D0',
               fc='#7A56D0', fill=False, lw=linewidth)
    ax.add_patch(c)
    line(ax, x, x, y - not_radius, y + not_radius, plot_params, '#7A56D0')
    line(ax, x - not_radius, x + not_radius, y, y, plot_params, '#7A56D0')
    return

def cdot(ax:Axes, x:float, y:float, plot_params:dict, dotcolor:str='#7A56D0'):
    """
    绘制控制位那个点
    Args:
        ax (Axes): 绘图对象
        x (float): 对应的圆心横坐标
        y (float): 对应的圆心纵坐标
        plot_params (dict): 基本参数信息
        dotcolor (str, optional): 设置点的颜色，默认值是'#7A56D0'.
    """
    Circle = patches.Circle
    control_radius = plot_params['control_radius']
    scale = plot_params['scale']
    linewidth = plot_params['linewidth']
    c = Circle((x, y), control_radius*scale,
        ec=dotcolor, fc=dotcolor, fill=True, lw=linewidth, zorder=2)
    ax.add_patch(c)
    return

def swapx(ax:Axes, x:float, y:float, plot_params:dict):
    """
    绘制交换门
    Args:
        ax (Axes): 绘图对象
        x (float): 绘制❌中心位置的横坐标
        y (float): 绘制❌中心位置的纵坐标
        plot_params (dict): 基本参数信息
    """
    d = plot_params['swap_delta']
    line(ax, x-d, x+d, y-d, y+d, plot_params, linecolor='#7A56D0')
    line(ax, x-d, x+d, y+d, y-d, plot_params, linecolor='#7A56D0')
    return

def setup_figure(nq:int, ng:int, gate_grid:np.array, wire_grid:np.array, plot_params:dict):
    """
    设置图形的基本信息
    Args:
        nq (int): 比特数
        ng (int): 门序列列数，主要是设置整个图的宽度
        gate_grid (np.array): 整个图的所有点的横坐标
        wire_grid (np.array): 整个图的所有点的纵坐标
        plot_params (dict): 基本参数信息
    """
    scale = plot_params['scale']
    fig = plt.figure(
        figsize=(ng * scale, nq * scale),
        facecolor='w',
        edgecolor='w'
    )
    ax = fig.add_subplot(1, 1, 1,frameon=True)
    # fig.tight_layout()
    ax.set_axis_off()
    offset = 0.5*scale
    ax.set_xlim(gate_grid[0] - offset, gate_grid[-1] + offset)
    ax.set_ylim(wire_grid[0] - offset, wire_grid[-1] + offset)
    ax.set_aspect('equal')
    return fig,ax

def draw_wires(ax:Axes, nq:int, gate_grid: np.array, wire_grid:np.array, plot_params:dict, linecolor:str, measured:dict={}):
    """
    绘制线路图中横线
    Args:
        ax (Axes): 绘图对象
        nq (int): 比特数
        gate_grid (np.array): 整个图的所有点的横坐标
        wire_grid (np.array): 整个图的所有点的纵坐标
        plot_params (dict): 基本参数信息
        linecolor (str): 线段的颜色
        measured (dict, optional): 测量门位置信息
    """
    scale = plot_params['scale']
    for i in range(nq):
        line(ax, gate_grid[0] - scale, gate_grid[-1] + scale, wire_grid[i], wire_grid[i], plot_params, linecolor)
        
    return

def draw_labels(ax:Axes, labels:list, inits:dict, gate_grid:list, wire_grid:np.array, plot_params:dict, textcolor:str):
    """
    每根线谱前对应的标签
    Args:
        ax (Axes): 绘图对象
        labels (list): 里面元素都是字符串，列举出每一个比特的标签
        inits (dict): 线路图中每一条线前面的标签与索引的关系
        gate_grid (list): 整个图的所有点的横坐标
        wire_grid (np.array): 整个图的所有点的纵坐标
        plot_params (dict): 基本参数信息
        textcolor (str): 填写内容的颜色
    """
    scale = plot_params['scale']
    label_buffer = plot_params['label_buffer']
    nq = len(labels)
    for i in range(nq):
        j = get_flipped_index(labels[i], labels)
        text(ax, gate_grid[0] - label_buffer * scale, wire_grid[j], render_label(labels[i], inits), plot_params, textcolor)
    return

def get_flipped_index(target:str, labels:list)->int:
    """
    获取当前门对应的比特位置索引
    Args:
        target (str): 门的名称
        labels (list): 里面元素都是字符串，列举出每一个比特的标签

    Returns:
        int: 对应整个线路图中纵坐标对应的索引值
    """
    nq = len(labels)
    i = labels.index(target)
    # nq-i-1是因为plt画图是：从下到上逐渐增大，但是比特位需要是从上到下是逐渐增大
    return nq-i-1

def get_flipped_indices(targets:list, labels:list)->list: 
    """
    获取多个门位置的比特位索引值
    Args:
        targets (list): 门序列，主要是用于处理多个控制位
        labels (list): 里面元素都是字符串，列举出每一个比特的标签

    Returns:
        list: 门序列中对应的比特位索引
    """
    return [get_flipped_index(t, labels) for t in targets]

def render_label(label:str, inits:dict={}):
    """
    绘制前面标签内容
    Args:
        label (str): 在当前代码中比特位的标签
        inits (dict, optional): 线路图中每一条线前面的标签与索引的关系

    Returns:
        str: Latex字符串代码
    """
    if label in inits:
        s = inits[label]
        if s is None:
            return ''
        else:
            return r'$q_%s|0\rangle$' % inits[label]
    return r'$q_%s|0\rangle$' % label
