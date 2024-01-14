class Solution:
    def outerTrees(self, trees: list[list[int]]) -> list[list[int]]:
        output = []
        up, down, left, right = trees[0], trees[0], trees[0], trees[0]
        up_cord, down_cord, right_cord, left_cord = None, None, None, None
        for t in trees:
            if t[1] >= up[1]:
                up_cord = t[1]
                up = t
            if t[1] <= down[1]:
                down_cord = t[1]
                down = t
            if t[0] >= right[0]:
                right_cord = t[0]
                right = t
            if t[0] <= left[0]:
                left_cord = t[0]
                left = t

        up_l, up_r, dw_l, dw_r, lft_u, lft_d, rt_u, rt_d = None, None, None, None, None, None, None, None
        for t in trees:
            if t[1] == up_cord:
                if t not in output:
                    output.append(t)
                if not up_l:
                    if t[0] <= up[0]:
                        up_l = t
                elif t[0] <= up_l[0]:
                    up_l = t
                if not up_r:
                    if t[0] >= up[0]:
                        up_r = t
                elif t[0] >= up_r[0]:
                    up_r = t

        for t in trees:
            if t[1] == down_cord:
                if t not in output:
                    output.append(t)
                if not dw_l:
                    if t[0] <= down[0]:
                        dw_l = t
                elif t[0] <= dw_l[0]:
                    dw_l = t
                if not dw_r:
                    if t[0] >= down[0]:
                        dw_r = t
                elif t[0] >= dw_r[0]:
                    dw_r = t
        for t in trees:
            if t[0] == left_cord:
                if t not in output:
                    output.append(t)
                if not lft_u:
                    if t[1] >= left[1]:
                        lft_u = t
                elif t[1] >= lft_u[1]:
                    lft_u = t
                if not lft_d: #ignoring the bug caused by [0,0] == false, while as setting [0,0] must be a vertex
                    if t[1] <= left[1]:
                        lft_d = t
                elif t[1] <= lft_d[1]:
                    lft_d = t
        for t in trees:
            if t[0] == right_cord:
                if t not in output:
                    output.append(t)
                if not rt_u:
                    if t[1] >= right[1]:
                        rt_u = t
                elif t[1] >= rt_u[1]:
                    rt_u = t
                if not rt_d:
                    if t[1] <= right[1]:
                        rt_d = t
                elif t[1] <= rt_d[1]:
                    rt_d = t

        # print(up_l, up_r, dw_l, dw_r, lft_u, lft_d, rt_u, rt_d)

        top_left, top_right, down_left, down_right = [], [], [], []
        for i in trees:
            if i not in output:
                if lft_u[0] <= i[0] <= up_l[0] and lft_u[1] <= i[1] <= up_l[1]:
                    top_left.append(i)
                if up_r[0] <= i[0] <= rt_u[0] and rt_u[1] <= i[1] <= up_r[1]:
                    top_right.append(i)
                if lft_d[0] <= i[0] <= dw_l[0] and lft_d[1] >= i[1] >= dw_l[1]:
                    down_left.append(i)
                if dw_r[0] <= i[0] <= rt_d[0] and dw_r[1] <= i[1] <= rt_d[1]:
                    down_right.append(i)

        down_right.sort()
        down_left.sort()
        top_left.sort()
        top_right.sort()

        # treat top left corner
        start, end = up_l, lft_u
        end_get = []
        if start is not end and (start[1] - end[1]) != 0:
            tan = (start[0] - end[0]) / (start[1] - end[1])
            while True:
                for j in top_left:
                    if j not in output and (start[1] - j[1]) != 0:
                        new_tan = (start[0] - j[0]) / (start[1] - j[1])
                        if start[0] - j[0] >= 0 and new_tan > tan:
                            tan = new_tan
                            end = j
                            end_get = [end]
                        elif start[0] - j[0] >= 0 and new_tan == tan:
                            if not end_get:
                                end = j
                            end_get.append(j)
                if end != lft_u or len(end_get) > 1:
                    output.extend(end_get)
                    end_get = []
                    start, end = end, lft_u
                    if (start[1] - end[1]) != 0: tan = (start[0] - end[0]) / (start[1] - end[1])
                else:
                    break

        # treat top right corner
        start, end = up_r, rt_u
        end_get = []
        if start is not end and (start[1] - end[1]) != 0:
            tan = (end[0] - start[0]) / (start[1] - end[1])
            while True:
                for j in top_right:
                    if j not in output and (start[1] - j[1]) != 0:
                        new_tan = (j[0] - start[0]) / (start[1] - j[1])
                        if j[0] - start[0] >= 0 and new_tan > tan:
                            tan = new_tan
                            end = j
                            end_get = [end]
                        if j[0] - start[0] >= 0 and new_tan == tan:
                            if not end_get:
                                end = j
                            end_get.append(j)
                if end != rt_u or len(end_get) > 1:
                    output.extend(end_get)
                    end_get = []
                    start, end = end, rt_u
                    if (start[1] - end[1]) != 0: tan = (end[0] - start[0]) / (start[1] - end[1])
                else:
                    break

        # treat down left corner
        start, end = lft_d, dw_l
        end_get = []
        if start is not end and (end[0] - start[0]) != 0:
            tan = (start[1] - end[1]) / (end[0] - start[0])
            while True:
                for j in down_left:
                    if j not in output and (j[0] - start[0]) != 0:
                        new_tan = (start[1] - j[1]) / (j[0] - start[0])
                        if start[1] - j[1] >= 0 and new_tan > tan:
                            tan = new_tan
                            end = j
                            end_get = [end]
                        elif start[1] - j[1] >= 0 and new_tan == tan:
                            if not end_get:
                                end = j
                            end_get.append(j)
                if end != dw_l or len(end_get) > 1:
                    output.extend(end_get)
                    end_get = []
                    start, end = end, dw_l
                    if (end[0] - start[0]) != 0: tan = (start[1] - end[1]) / (end[0] - start[0])
                else:
                    break
        # treat down right corner
        start, end = rt_d, dw_r
        end_get = []
        if start is not end and (start[0] - end[0]) != 0:
            tan = (start[1] - end[1]) / (start[0] - end[0])
            while True:
                for j in down_right:
                    if j not in output and (start[0] - j[0]) != 0:
                        new_tan = (start[1] - j[1]) / (start[0] - j[0])
                        if start[1] - j[1] >= 0 and new_tan > tan:
                            tan = new_tan
                            end = j
                            end_get = [end]
                        elif start[1] - j[1] >= 0 and new_tan == tan:
                            if not end_get:
                                end = j
                            end_get.append(j)
                if end != dw_r or len(end_get) > 1:
                    output.extend(end_get)
                    end_get = []
                    start, end = end, dw_r
                    if (start[0] - end[0]) != 0: tan = (start[1] - end[1]) / (start[0] - end[0])
                else:
                    break
        output_f = []
        for i in output:
            if i not in output_f:
                output_f.append(i)
        return output_f