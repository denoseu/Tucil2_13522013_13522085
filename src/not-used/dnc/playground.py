# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# def mid(point1, point2):
#     return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

# # 4 control points
# P0 = (0,0)
# P1 = (3,3)
# P2 = (6,4)
# P3 = (9,3)
# P4 = (12,0)
# # Extract x and y coordinates of control points
# X0 = [P0[0], P1[0], P2[0], P3[0], P4[0]]
# Y0 = [P0[1], P1[1], P2[1], P3[1], P4[1]]
# # Plot control points
# plt.plot(X0, Y0, 'ro-')


# # ITERATION 0
# mid01 = mid(P0,P1)
# mid02 = mid(P1,P2)
# mid03 = mid(P2,P3)
# mid04 = mid(P3,P4)
# middle0 = mid(mid02, mid03)
# b0_x = [mid01[0], mid02[0], mid03[0], mid04[0]]
# b0_y = [mid01[1], mid02[1], mid03[1], mid04[1]]
# # # b00_x = [mid012[0], mid023[0]]
# # # b00_y = [mid012[1], mid023[1]]
# first_x = [P0[0], middle0[0], P4[0]]
# first_y = [P0[1], middle0[1], P4[1]]
# # # Plot control points
# plt.plot(b0_x, b0_y, 'g--')
# # # plt.plot(b00_x, b00_y, 'g--')
# plt.plot(first_x, first_y, 'go-')



# # ITERATION 1
# mid11 = mid(mid01, mid02)
# # mid12 = mid(mid01, mid012)
# # mid13 = mid(mid023, mid03)
# # mid14 = mid(mid03, P3)
# # mid112 = mid(mid11, mid12)
# # mid120 = mid(mid12, middle0)
# # mid103 = mid(middle0, mid13)
# # mid134 = mid(mid13, mid14)
# # middle11 = mid(mid112, mid120)
# # middle12 = mid(mid103, mid134)
# # # Extract x and y coordinates 
# b1_x = [mid11[0]]
# b1_y = [mid11[1]]
# # # b1_x = [mid11[0], mid12[0], middle0[0], mid13[0], mid14[0]]
# # # b1_y = [mid11[1], mid12[1], middle0[1], mid13[1], mid14[1]]
# # # b01_x = [P0[0], mid112[0], mid120[0], middle0[0], mid103[0], mid134[0], P3[0]]
# # # b01_y = [P0[1], mid112[1], mid120[1], middle0[1], mid103[1], mid134[1], P3[1]]
# # second_x = [P0[0], middle11[0], middle0[0], middle12[0], P3[0]]
# # second_y = [P0[1], middle11[1], middle0[1], middle12[1], P3[1]]
# # # Plot control points
# plt.plot(b1_x, b1_y, 'b--')
# # # plt.plot(b01_x, b01_y, 'b--')
# # plt.plot(second_x, second_y, 'bo-')


# # # ITERATION 2
# # mid21 = mid(P0, mid11)
# # mid22 = mid(mid120, middle0)
# # mid23 = mid(middle0, mid103)
# # mid24 = mid(mid03, P3)
# # mid212 = mid(mid21, mid112)
# # mid234 = mid(mid134, mid24)
# # # Extract x and y coordinates 
# # b2_x = [mid11[0], mid12[0], middle0[0], mid13[0], mid14[0]]
# # b2_y = [mid11[1], mid12[1], middle0[1], mid13[1], mid14[1]]
# # b02_x = [P0[0], mid112[0], mid120[0], middle0[0], mid103[0], mid134[0], P3[0]]
# # b02_y = [P0[1], mid112[1], mid120[1], middle0[1], mid103[1], mid134[1], P3[1]]
# # third_y = [P0[1], mid212[1], middle11[1], mid22[1], middle0[1], mid23[1], middle12[1], mid234[1], P3[1]]
# # third_x = [P0[0], mid212[0], middle11[0], mid22[0], middle0[0], mid23[0], middle12[0], mid234[0], P3[0]]
# # # Plot control points
# # # plt.plot(b1_x, b1_y, 'b--')
# # # plt.plot(b01_x, b01_y, 'b--')
# # plt.plot(third_x, third_y, 'ro-')


# # Annotate control points
# for i, (x, y) in enumerate([P0, P1, P2, P3]):
#     plt.text(x, y, f'P{i}', fontsize=12, ha='right')

# for i, (x, y) in enumerate([mid01, mid02, mid03, mid04]):
#     plt.text(x, y, f'mid0{i+1}', fontsize=8, ha='right')

# for i, (x, y) in enumerate([mid11]):
#     plt.text(x, y, f'mid1{i+1}', fontsize=8, ha='right')

# # Set plot title and labels
# plt.title('Bezier Curve Control Points')
# plt.xlabel('X')
# plt.ylabel('Y')

# # Set equal aspect ratio
# plt.gca().set_aspect('equal', adjustable='box')

# # Show plot
# plt.grid(True)
# plt.show()


# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# def mid(point1, point2):
#     return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

# # 4 control points
# P0 = (0,0)
# P1 = (0,5)
# P2 = (5,5)
# P3 = (5,0)
# # Extract x and y coordinates of control points
# X0 = [P0[0], P1[0], P2[0], P3[0]]
# Y0 = [P0[1], P1[1], P2[1], P3[1]]
# # Plot control points
# plt.plot(X0, Y0, 'ro-')


# # ITERATION 0
# mid01 = mid(P0,P1)
# mid02 = mid(P1,P2)
# mid03 = mid(P2,P3)
# mid012 = mid(mid01,mid02)
# mid023 = mid(mid02,mid03)
# middle0 = mid(mid012, mid023)
# # middle1 = mid((mid(mid01,mid02)), (mid(mid02,mid03)))
# # Extract x and y coordinates of control points
# # b0_x = [mid01[0], mid02[0], mid03[0]]
# # b0_y = [mid01[1], mid02[1], mid03[1]]
# # b00_x = [mid012[0], mid023[0]]
# # b00_y = [mid012[1], mid023[1]]
# first_x = [P0[0], middle0[0], P3[0]]
# first_y = [P0[1], middle0[1], P3[1]]
# # Plot control points
# # plt.plot(b0_x, b0_y, 'g--')
# # plt.plot(b00_x, b00_y, 'g--')
# plt.plot(first_x, first_y, 'go-')



# # ITERATION 1
# mid11 = mid(P0, mid01)
# mid12 = mid(mid01, mid012)
# mid13 = mid(mid023, mid03)
# mid14 = mid(mid03, P3)
# mid112 = mid(mid11, mid12)
# mid120 = mid(mid12, middle0)
# mid103 = mid(middle0, mid13)
# mid134 = mid(mid13, mid14)
# middle11 = mid(mid112, mid120)
# middle12 = mid(mid103, mid134)
# # Extract x and y coordinates 
# # b1_x = [mid11[0], mid12[0], middle0[0], mid13[0], mid14[0]]
# # b1_y = [mid11[1], mid12[1], middle0[1], mid13[1], mid14[1]]
# # b01_x = [P0[0], mid112[0], mid120[0], middle0[0], mid103[0], mid134[0], P3[0]]
# # b01_y = [P0[1], mid112[1], mid120[1], middle0[1], mid103[1], mid134[1], P3[1]]
# second_x = [P0[0], middle11[0], middle0[0], middle12[0], P3[0]]
# second_y = [P0[1], middle11[1], middle0[1], middle12[1], P3[1]]
# # Plot control points
# # plt.plot(b1_x, b1_y, 'b--')
# # plt.plot(b01_x, b01_y, 'b--')
# plt.plot(second_x, second_y, 'bo-')


# # ITERATION 2
# mid21 = mid(P0, mid11)
# mid22 = mid(mid120, middle0)
# mid23 = mid(middle0, mid103)
# mid24 = mid(mid03, P3)
# mid212 = mid(mid21, mid112)
# mid234 = mid(mid134, mid24)
# # Extract x and y coordinates 
# b2_x = [mid11[0], mid12[0], middle0[0], mid13[0], mid14[0]]
# b2_y = [mid11[1], mid12[1], middle0[1], mid13[1], mid14[1]]
# b02_x = [P0[0], mid112[0], mid120[0], middle0[0], mid103[0], mid134[0], P3[0]]
# b02_y = [P0[1], mid112[1], mid120[1], middle0[1], mid103[1], mid134[1], P3[1]]
# third_y = [P0[1], mid212[1], middle11[1], mid22[1], middle0[1], mid23[1], middle12[1], mid234[1], P3[1]]
# third_x = [P0[0], mid212[0], middle11[0], mid22[0], middle0[0], mid23[0], middle12[0], mid234[0], P3[0]]
# # Plot control points
# # plt.plot(b1_x, b1_y, 'b--')
# # plt.plot(b01_x, b01_y, 'b--')
# plt.plot(third_x, third_y, 'ro-')















# # Annotate control points
# for i, (x, y) in enumerate([P0, P1, P2, P3]):
#     plt.text(x, y, f'P{i}', fontsize=12, ha='right')

# # Set plot title and labels
# plt.title('Bezier Curve Control Points')
# plt.xlabel('X')
# plt.ylabel('Y')

# # Set equal aspect ratio
# plt.gca().set_aspect('equal', adjustable='box')

# # Show plot
# plt.grid(True)
# plt.show()


# import matplotlib.pyplot as plt
# import copy

# def mid(point1, point2):
#     return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

# def midList(listOfPoints):
#     return ((listOfPoints[0][0] + listOfPoints[1][0]) / 2, (listOfPoints[0][1] + listOfPoints[1][1]) / 2)

# # Input n titik
# n = int(input("Masukan jumlah titik yang hendak dimasukkan: "))

# while (n < 2):
#     print("\nUntuk membuat kurva masukan 2 atau lebih titik!")
#     n = int(input("Masukan jumlah titik yang hendak dimasukkan: "))

# # Input koordinat poin-poin
# x_start, y_start = map(float, input("Masukan start point (x,y): ").split(","))
# points = [(x_start, y_start)]

# # Input control points
# for i in range(n-2):
#     x, y = map(float, input("Masukan control point {}: (x,y): ".format(i+1)).split(","))
#     points.append((x, y))

# x_end, y_end = map(float, input("Masukan end point (x,y): ").split(","))
# points.append((x_end, y_end))

# print("")

# iterate = 0
# graph_points = []
# graph_points.append(points[0])
# graph_points.append(points[-1])
# next_points = []
# before_next_points = []
# next_points.append(points[0])
# print("next now:")
# print(next_points)
# buffer = copy.copy(points)
# while len(buffer) >= 1 and iterate == 0 :
#     if len(buffer) >= 2 :
#         mid = midList(buffer[:2])
#         print("\nto compare:")
#         print(buffer[:2])
#         print("\nresult:")
#         print(mid)
#         before_next_points.append(mid)
#         print("\nin before now:")
#         print(before_next_points)
#         del buffer[0]
#         print("\nin buffer now:")
#         print(buffer)
#     else:
#         next_points += buffer
#         print(next_points)
#         del buffer[0]

# print("\n- NEXT STEP -")     

# buffer = copy.copy(before_next_points)
# to = len(next_points) // 2 
# next_points.insert(to, buffer[-1])
# to = len(next_points) // 2 
# next_points.insert(to, buffer[0])
# print("\nin next now:")
# print(next_points)

# before_next_points = []
# while len(buffer) > 0 :
#     if len(buffer) >= 2 :
#         mid = midList(buffer[:2])
#         print("\nto compare:")
#         print(buffer[:2])
#         print("\nresult:")
#         print(mid)
#         before_next_points.append(mid)
#         print("\nin before now:")
#         print(before_next_points)
#         del buffer[0]
#         print("\nin buffer now:")
#         print(buffer)
#     else:
#         # to = len(next_points) // 2 
#         # next_points.insert(to, buffer[0])
#         print(next_points)
#         del buffer[0]

# print("\n- NEXT STEP -")     

# buffer = copy.copy(before_next_points)
# to = len(next_points) // 2 
# next_points.insert(to, buffer[-1])
# to = len(next_points) // 2 
# next_points.insert(to, buffer[0])
# print("\nin next now:")
# print(next_points)

# before_next_points = []
# while len(buffer) > 0 :
#     if len(buffer) >= 2 :
#         mid = midList(buffer[:2])
#         print("\nto compare:")
#         print(buffer[:2])
#         print("\nresult:")
#         print(mid)
#         before_next_points.append(mid)
#         print("\nin before now:")
#         print(before_next_points)
#         del buffer[0]
#         print("\nin buffer now:")
#         print(buffer)
#     else:
#         # to = len(next_points) // 2 
#         # next_points.insert(to, before_next_points[0])
#         print(next_points)
#         del buffer[0]

# print("\nin next now:")
# to_next = len(next_points) // 2 
# next_points.insert(to_next, before_next_points[0])
# print(next_points)

# print("\nin graph now:")
# to_graph = len(graph_points) // 2
# graph_points.insert(to_graph, before_next_points[0])
# print(graph_points)

# second_x = [next_points[0] for point in next_points]
# second_y = [next_points[1] for point in next_points]
# plt.plot(second_x, second_y, 'bo-')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Plot of Points')
# plt.grid(True)
# plt.axis('equal')  # Ensure equal scaling on both axes
# plt.plot([point[0] for point in points], [point[1] for point in points], 'ro-', label='Control Points')
# plt.plot([point[0] for point in next_points], [point[1] for point in next_points], 'b--', label='Next Points')
# plt.plot([point[0] for point in graph_points], [point[1] for point in graph_points], 'go-', label='graph iteration 0')
# plt.show()

# print("")

# iterate = 1

# next_points = []
# before_next_points = []
# next_points.append(points[0])
# print("next now:")
# print(next_points)
# buffer = copy.copy(points)
# while len(buffer) >= 1 and iterate == 0 :
#     if len(buffer) >= 2 :
#         mid = midList(buffer[:2])
#         print("\nto compare:")
#         print(buffer[:2])
#         print("\nresult:")
#         print(mid)
#         before_next_points.append(mid)
#         print("\nin before now:")
#         print(before_next_points)
#         del buffer[0]
#         print("\nin buffer now:")
#         print(buffer)
#     else:
#         next_points += buffer
#         print(next_points)
#         del buffer[0]

# print("\n- NEXT STEP -")     

# buffer = copy.copy(before_next_points)
# to = len(next_points) // 2 
# next_points.insert(to, buffer[-1])
# to = len(next_points) // 2 
# next_points.insert(to, buffer[0])
# print("\nin next now:")
# print(next_points)

# before_next_points = []
# while len(buffer) > 0 :
#     if len(buffer) >= 2 :
#         mid = midList(buffer[:2])
#         print("\nto compare:")
#         print(buffer[:2])
#         print("\nresult:")
#         print(mid)
#         before_next_points.append(mid)
#         print("\nin before now:")
#         print(before_next_points)
#         del buffer[0]
#         print("\nin buffer now:")
#         print(buffer)
#     else:
#         # to = len(next_points) // 2 
#         # next_points.insert(to, buffer[0])
#         print(next_points)
#         del buffer[0]

# print("\n- NEXT STEP -")     

# buffer = copy.copy(before_next_points)
# to = len(next_points) // 2 
# next_points.insert(to, buffer[-1])
# to = len(next_points) // 2 
# next_points.insert(to, buffer[0])
# print("\nin next now:")
# print(next_points)

# before_next_points = []
# while len(buffer) > 0 :
#     if len(buffer) >= 2 :
#         mid = midList(buffer[:2])
#         print("\nto compare:")
#         print(buffer[:2])
#         print("\nresult:")
#         print(mid)
#         before_next_points.append(mid)
#         print("\nin before now:")
#         print(before_next_points)
#         del buffer[0]
#         print("\nin buffer now:")
#         print(buffer)
#     else:
#         # to = len(next_points) // 2 
#         # next_points.insert(to, before_next_points[0])
#         print(next_points)
#         del buffer[0]

# print("\nin next now:")
# to_next = len(next_points) // 2 
# next_points.insert(to_next, before_next_points[0])
# print(next_points)

# print("\nin graph now:")
# to_graph = len(graph_points) // 2
# graph_points.insert(to_graph, before_next_points[0])
# print(graph_points)

# second_x = [next_points[0] for point in next_points]
# second_y = [next_points[1] for point in next_points]
# plt.plot(second_x, second_y, 'bo-')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Plot of Points')
# plt.grid(True)
# plt.axis('equal')  # Ensure equal scaling on both axes
# plt.plot([point[0] for point in points], [point[1] for point in points], 'ro-', label='Control Points')
# plt.plot([point[0] for point in next_points], [point[1] for point in next_points], 'b--', label='Next Points')
# plt.plot([point[0] for point in graph_points], [point[1] for point in graph_points], 'go-', label='graph iteration 0')
# plt.show()


# import matplotlib.pyplot as plt
# import copy

# def mid(point1, point2):
#     return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

# def midList(listOfPoints):
#     return ((listOfPoints[0][0] + listOfPoints[1][0]) / 2, (listOfPoints[0][1] + listOfPoints[1][1]) / 2)

# def recursive_iteration(points, iterate, graph_points=[]):
#     if iterate == 0:
#         graph_points.append(points[0])
#         graph_points.append(points[-1])
#         next_points = []
#         next_points.append(points[0])
#         buffer = copy.copy(points)
#         while len(buffer) >= 1:
#             if len(buffer) >= 2:
#                 mid_point = midList(buffer[:2])
#                 graph_points.append(mid_point)
#                 del buffer[0]
#             else:
#                 next_points += buffer
#                 del buffer[0]
#         to_insert = len(next_points) // 2
#         next_points.insert(to_insert, graph_points[-1])
#         to_insert = len(next_points) // 2
#         next_points.insert(to_insert, graph_points[0])
#         recursive_iteration(next_points, iterate + 1, graph_points)
#     else:
#         buffer = copy.copy(graph_points)
#         while len(buffer) > 0:
#             if len(buffer) >= 2:
#                 mid_point = midList(buffer[:2])
#                 graph_points.append(mid_point)
#                 del buffer[0]
#             else:
#                 to_insert = len(points) // 2
#                 points.insert(to_insert, buffer[0])
#                 del buffer[0]
#         to_insert = len(points) // 2
#         points.insert(to_insert, graph_points[-1])
#         to_insert = len(points) // 2
#         points.insert(to_insert, graph_points[0])
#         plt.plot([point[0] for point in points], [point[1] for point in points], 'go-', label=f'graph iteration {iterate}')
#         plt.plot([point[0] for point in points], [point[1] for point in points], 'ro-', label='Control Points')
#         plt.xlabel('X')
#         plt.ylabel('Y')
#         plt.title('Plot of Points and Graph Iterations')
#         plt.grid(True)
#         plt.axis('equal')  # Ensure equal scaling on both axes
#         plt.legend()
#         plt.show()

# # Input n titik
# n = int(input("Masukan jumlah titik yang hendak dimasukkan: "))

# while (n < 2):
#     print("\nUntuk membuat kurva masukan 2 atau lebih titik!")
#     n = int(input("Masukan jumlah titik yang hendak dimasukkan: "))

# # Input koordinat poin-poin
# x_start, y_start = map(float, input("Masukan start point (x,y): ").split(","))
# points = [(x_start, y_start)]

# # Input control points
# for i in range(n-2):
#     x, y = map(float, input("Masukan control point {}: (x,y): ".format(i+1)).split(","))
#     points.append((x, y))

# x_end, y_end = map(float, input("Masukan end point (x,y): ").split(","))
# points.append((x_end, y_end))

# recursive_iteration(points, 0)












































# # import matplotlib.pyplot as plt
# # from matplotlib.animation import FuncAnimation

# # def mid(point1, point2):
# #     return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

# # def plot_bezier_recursive(P0, P1, P2, P3, n, segments):
# #     if n == 0:
# #         segments.append(([P0[0], P3[0]], [P0[1], P3[1]]))  # Add the line between P0 and P3 to segments
# #     else:
# #         mid01 = mid(P0, P1)
# #         mid12 = mid(P1, P2)
# #         mid23 = mid(P2, P3)
# #         mid012 = mid(mid01, mid12)
# #         mid123 = mid(mid12, mid23)
# #         mid0123 = mid(mid012, mid123)
        
# #         plot_bezier_recursive(P0, mid01, mid012, mid0123, n - 1, segments)
# #         plot_bezier_recursive(mid0123, mid123, mid23, P3, n - 1, segments)

# # def bezier_curve_animation(P0, P1, P2, P3, iterations):
# #     segments = []
# #     fig, ax = plt.subplots()
# #     ax.set_xlabel('X-axis')
# #     ax.set_ylabel('Y-axis')
# #     ax.set_title('Bézier Curve Animation')
# #     ax.grid(True)
# #     ax.axis('equal')

# #     def update(frame):
# #         plt.cla()
        
# #         # Plot control points
# #         plt.plot([P0[0], P1[0], P2[0], P3[0]], [P0[1], P1[1], P2[1], P3[1]], 'ro-')
# #         plt.text(P0[0], P0[1], 'P0', fontsize=12, ha='right')
# #         plt.text(P1[0], P1[1], 'P1', fontsize=12, ha='right')
# #         plt.text(P2[0], P2[1], 'P2', fontsize=12, ha='right')
# #         plt.text(P3[0], P3[1], 'P3', fontsize=12, ha='right')

# #         # Plot Bezier curve segments iteratively up to the current frame
# #         plot_bezier_recursive(P0, P1, P2, P3, frame + 1, segments)
# #         for segment in segments:
# #             plt.plot(segment[0], segment[1], 'b-')
        
# #         # Set plot title and labels
# #         plt.title(f'Bezier Curve Iteration {frame + 1}')
# #         plt.xlabel('X')
# #         plt.ylabel('Y')
    
# #         # Set equal aspect ratio
# #         plt.gca().set_aspect('equal', adjustable='box')

# #     # Create animation
# #     ani = FuncAnimation(fig, update, frames=iterations, interval=500)

# #     plt.show()

# # # 4 control points
# # P0 = (0,0)
# # P1 = (0,5)
# # P2 = (5,5)
# # P3 = (5,0)

# # # Number of iterations
# # n = 6

# # # Run the animation
# # bezier_curve_animation(P0, P1, P2, P3, n)


# import matplotlib.pyplot as plt

# def mid(point1, point2):
#     return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

# def plot_bezier_recursive(P0, P1, P2, P3, n):
#     if n == 0:
#         plt.plot([P0[0], P3[0]], [P0[1], P3[1]], 'ro-')  # Plot the line between P0 and P3
#     else:
#         mid01 = mid(P0, P1)
#         mid12 = mid(P1, P2)
#         mid23 = mid(P2, P3)
#         mid012 = mid(mid01, mid12)
#         mid123 = mid(mid12, mid23)
#         mid0123 = mid(mid012, mid123)
        
#         plot_bezier_recursive(P0, mid01, mid012, mid0123, n - 1)
#         plot_bezier_recursive(mid0123, mid123, mid23, P3, n - 1)

# # 4 control points
# P0 = (0,0)
# P1 = (1,1)
# P2 = (2,1)
# P3 = (4,2)

# # Number of iterations
# n = 3

# # Plot control points
# plt.plot([P0[0], P1[0], P2[0], P3[0]], [P0[1], P1[1], P2[1], P3[1]], 'ro-')

# # Plot Bezier curve recursively
# plot_bezier_recursive(P0, P1, P2, P3, n)

# # Annotate control points
# for i, (x, y) in enumerate([P0, P1, P2, P3]):
#     plt.text(x, y, f'P{i}', fontsize=12, ha='right')

# # Set plot title and labels
# plt.title('Bezier Curve Control Points')
# plt.xlabel('X')
# plt.ylabel('Y')

# # Set equal aspect ratio
# plt.gca().set_aspect('equal', adjustable='box')

# # Show plot
# plt.grid(True)
# plt.show()

# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# import sys

# # Set the recursion limit
# sys.setrecursionlimit(100)

# def mid(point1, point2):
#     return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

# def midList(listOfPoints):
#     return ((listOfPoints[0][0] + listOfPoints[1][0]) / 2, (listOfPoints[0][1] + listOfPoints[1][1]) / 2)

# def plot_points(points, graph_points):
#     # Extract x and y coordinates from the points
#     x_graph = [point[0] for point in graph_points]
#     y_graph = [point[1] for point in graph_points]

#     x_points = [point[0] for point in points]
#     y_points = [point[1] for point in points]

#     # Plot the points
#     plt.plot(x_graph, y_graph, 'bo-')  # 'ro-' represents red circles connected by lines
#     plt.plot(x_points, y_points, 'ro-')  # 'ro-' represents red circles connected by lines
#     plt.xlabel('X')
#     plt.ylabel('Y')
#     plt.title('Graph of Points')
#     plt.grid(True)
#     plt.axis('equal')  # Ensure equal scaling on both axes
#     plt.show()

# # Input n titik
# n = int(input("Masukan jumlah titik yang hendak dimasukkan: "))

# while (n < 2):
#     print("\nUntuk membuat kurva masukan 2 atau lebih titik!")
#     n = int(input("Masukan jumlah titik yang hendak dimasukkan: "))

# # Input koordinat poin-poin
# x_start, y_start = map(float, input("Masukan start point (x,y): ").split(","))
# points = [(x_start, y_start)]

# # Input control points
# for i in range(n-2):
#     x, y = map(float, input("Masukan control point {}: (x,y): ".format(i+1)).split(","))
#     points.append((x, y))

# x_end, y_end = map(float, input("Masukan end point (x,y): ").split(","))
# points.append((x_end, y_end))

# print("Iterasi maksimum ialah n+1! (dengan n jumlah titik yang dimasukkan)")
# i = int(input("Masukan jumlah iterasi: "))
# while i > n+1 :
#     print("Iterasi maksimum ialah n+1! (dengan n jumlah titik yang dimasukkan)")
#     i = int(input("Masukan jumlah iterasi: "))


# def mid(point1, point2):
#     return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

# def recursive_midpoint(points, next_points):
#     if len(points) == 1:
#         return points[0], next_points
#     else:
#         midpoints = []
#         for i in range(len(points) - 1):
#             midpoints.append(mid(points[i], points[i+1]))
#         if len(midpoints) == 1:
#             to = len(next_points) // 2 
#             next_points.insert(to, midpoints[0])
#             # print("\nnext before: ", next_points)
#             # new_next_points = [next_points[0]] + left_next + midpoints + right_next + [next_points[-1]]
#             # print("\nnext now: ", next_points)
#         else:
#             # print("\nnext before: ", next_points)
#             # print("midpoints now: ", midpoints)
#             to = len(next_points) // 2 
#             next_points.insert(to, midpoints[-1])
#             next_points.insert(to, midpoints[0])
#             # print("\nnext in rec now: ", next_points)
#         return recursive_midpoint(midpoints, next_points)
    
# def make_the_next(points, next_points, middle):
#     going = [points[0]] + next_points + [points[-1]]
#     if len(going) % 2 == 0:
#         to = len(going) // 2
#         going.insert(to, middle)
#     return going

# def gather_graph_points(graph_points, middle_points):
#     if len(middle_points) == 1 and len(graph_points) == 2:
#         to = len(graph_points) // 2 
#         graph_points.insert(to, middle_points[0])
#         return graph_points
#     else:
#         mid_graph = len(graph_points) // 2 
#         left_half_graph = graph_points[:mid_graph+1]
#         right_half_graph = graph_points[mid_graph:]

#         mid_middle = len(middle_points) // 2 
#         left_half_middle = middle_points[:mid_middle]
#         right_half_middle = middle_points[mid_middle:]

#         return gather_graph_points(left_half_graph, left_half_middle)[:-1] + gather_graph_points(right_half_graph, right_half_middle)

# def divide_list_of_points(points, length):
#     num_points = len(points)
#     if num_points <= length:
#         return [points]
#     else:
#         midpoint = num_points // 2
#         left_half = points[:midpoint+1]
#         right_half = points[midpoint:]
#         return divide_list_of_points(left_half, length) + divide_list_of_points(right_half, length)

# def iterations(points, next_points, graph_points, iteration, i_now):
#     print(f"\nNOW ITERATION {i_now}")
#     plot_points(points, graph_points)
    
#     if iteration == 0:
#         return graph_points
#     elif len(next_points) <= len(points):
#         new_mids = []
#         new_midpoints, new_next_points = recursive_midpoint(points, next_points)
#         new_mids.append(new_midpoints)
#         # print("\nNew Mid : ",new_midpoints)
#         graph_points = gather_graph_points(graph_points, new_mids)
#         # print("\nNext: ", new_next_points)
#         # print("\nGraphs: ", graph_points)
#         return iterations(points, new_next_points, graph_points, iteration-1, i_now+1)
#     else:
#         top = graph_points[len(graph_points)//2]
#         # print(top)
#         next_points = make_the_next(points, next_points, top)
#         # print(next_points)
#         divided_next_points = divide_list_of_points(next_points, len(points))
#         # print("\ndivided?", divided_next_points)
#         # i = -1
#         each_next = []
#         new_mids = []
#         for part in divided_next_points:
#             # i += 1
#             # print("\npart: ", part)
#             # if i % 2 == 1:
#             new_midpoints, the_next = recursive_midpoint(part, [])
#             # print("\nNew Mid: ",new_midpoints)
#             new_mids.append(new_midpoints)
#                 # to = len(graph_points) // 2 + 1
#                 # new_mids.insert(to, new_midpoints)
#                 # print("\nNext: ", the_next)
#                 # print("\nMids: ", new_mids)
#                 # print("\nGraphs: ", graph_points)
#             # else:
#             #     new_midpoints, the_next = recursive_midpoint(part, [])
#             #     # print("\nNew Mid: ",new_midpoints)
#             #     new_mids.append(new_midpoints)
#             #     # to = len(graph_points) // 2 
#             #     # new_mids.insert(to, new_midpoints)
#             #     next_points.insert(0, points[0])
#             #     next_points.append(points[-1])
#             #     # print("\nLeft: ", new_left)
#             #     # print("\nRight: ", new_right)
#             #     # print("\nNext: ", the_next)
#             #     # print("\nMids: ", new_mids)
#             #     # print("\nGraphs: ", graph_points)
#             for next in the_next:
#                 each_next.append(next)

#         graph_points = gather_graph_points(graph_points, new_mids)
#         # print("\nGraphs: ", graph_points)
#         return iterations(points, each_next, graph_points, iteration-1, i_now+1)

# # def divide_list_of_points(next_points, iteration):







# # Example array of points
# # points = [(1.0, 0.0), (0.0, 3.0), (3.0, 6.0), (6.0, 6.0), (9.0, 3.0), (8.0, 0.0)]
# # points = [(0.0, 0.0), (2.0, 5.0), (6.0, 7.0), (10.0, 5.0), (12.0, 0.0)]
# # points = [(0.0, 0.0), (0.0, 8.0), (8.0, 8.0), (8.0, 0.0)]

# print("Points : ")
# print(points)
# next_points = []
# # next_points.append(points[0])
# # next_points.append(points[-1])
# print("\nnext start: ", next_points)
# graph_points = []
# graph_points.append(points[0])
# graph_points.append(points[-1])

# print("\n ITERATION 0")
# the_graph_points = iterations(points, next_points, graph_points, i, 0)

# # final_midpoint, next_points = recursive_midpoint(points, next_points)
# # print("Final Midpoint:", final_midpoint)
# # print("Next point:", next_points)
# # print("Graph points before:", graph_points)
# # to = len(graph_points) // 2
# # graph_points.insert(to, final_midpoint)
# # print("Graph points after:", graph_points)
# # plot_points(points, graph_points)
# # print(next_points)
# # next_points, graph_points = next_iteration(next_points, graph_points)
# # plot_points(points, graph_points)






# def gather_graph_points(graph_points, middle_points):
#     if len(middle_points) == 1 and len(graph_points) == 2:
#         to = len(graph_points) // 2 
#         graph_points.insert(to, middle_points[0])
#         return graph_points
#     else:
#         mid_graph = len(graph_points) // 2 
#         left_half_graph = graph_points[:mid_graph+1]
#         right_half_graph = graph_points[mid_graph:]

#         mid_middle = len(middle_points) // 2 
#         left_half_middle = middle_points[:mid_middle]
#         right_half_middle = middle_points[mid_middle:]

#         return gather_graph_points(left_half_graph, left_half_middle)[:-1] + gather_graph_points(right_half_graph, right_half_middle)

#         # for i in range(len(graph_points) - 1):
#         #     new_graph_points.append(graph_points[i])
#         #     new_graph_points.append(middle_points[i])
#         # new_graph_points.append(graph_points[-1])
#         # print("\nnew: "new_graph_points)
#         # return gather_graph_points(new_graph_points, [middle_points[i] for i in range(len(middle_points) - 1)])

# # Test cases
# # graph_points1 = ["P1", "P2"]
# # middle_points1 = ["Q1"]
# # print(gather_graph_points(graph_points1, middle_points1))  # Output: ['P1', 'Q1', 'P2']

# # graph_points2 = ["P1", "Q1", "P2"]
# # middle_points2 = ["R1", "R2"]
# # print(gather_graph_points(graph_points2, middle_points2))  # Output: ['P1', 'R1', 'Q1', 'R2', 'P2']

# # graph_points3 = ["P1", "R1", "Q1", "R2", "P2"]
# # middle_points3 = ["S1", "S2", "S3", "S4"]
# # print(gather_graph_points(graph_points3, middle_points3))  # Output: ['P1', 'S1', 'R1', 'S2', 'Q1', 'S3', 'R2', 'S4', 'P2']

# # graph_points4 = ["P1", "S1", "R1", "S2", "Q1", "S3", "R2", "S4", "P2"]
# # middle_points4 = ["T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8"]
# # print(gather_graph_points(graph_points4, middle_points4))  # Output: ['P1', 'T1', 'S1', 'T2', 'R1', 'T3', 'S2', 'T4', 'Q1', 'T5', 'S3', 'T6', 'R2', 'T7', 'S4', 'T8', 'P2']


# # # def gather_graph_points(graph_points, middle_points):
# # #     if len(middle_points) == 0:
# # #         return graph_points
# # #     else:
# # #         merged_points = []
# # #         for i in range(len(middle_points)):
# # #             merged_points.append(graph_points[i])
# # #             merged_points.append(middle_points[i])
# # #         merged_points.append(graph_points[-1])
        
# # #         return gather_graph_points(merged_points, [])

# # def merge_graph_points(graph_points1, graph_points2):
# #     merged_points = []
# #     i = 0
# #     j = 0
    
# #     # Merge the two lists by comparing elements
# #     while i < len(graph_points1) and j < len(graph_points2):
# #         if graph_points1[i] < graph_points2[j]:
# #             merged_points.append(graph_points1[i])
# #             i += 1
# #         else:
# #             merged_points.append(graph_points2[j])
# #             j += 1
    
# #     # Add remaining elements from the first list
# #     while i < len(graph_points1):
# #         merged_points.append(graph_points1[i])
# #         i += 1
    
# #     # Add remaining elements from the second list
# #     while j < len(graph_points2):
# #         merged_points.append(graph_points2[j])
# #         j += 1
    
# #     return merged_points

# # def divide_and_conquer_merge(graph_points):
# #     if len(graph_points) <= 1:
# #         return graph_points
    
# #     # Divide the list into two halves
# #     mid = len(graph_points) // 2
# #     left_half = graph_points[:mid]
# #     right_half = graph_points[mid:]
    
# #     # Recursively merge the two halves
# #     left_half = divide_and_conquer_merge(left_half)
# #     right_half = divide_and_conquer_merge(right_half)
    
# #     # Merge the two sorted halves
# #     return merge_graph_points(left_half, right_half)

# # # Example usage:
# # graph_points = [2, 4, 6, 8, 1, 3, 5, 7]
# # sorted_points = divide_and_conquer_merge(graph_points)
# # print(sorted_points)


# # Test the function with example iterations
# # graph_points_1 = ['P1', 'P2']
# # middle_points_1 = ['Q1']
# # result_1 = gather_graph_points(graph_points_1, middle_points_1)
# # print(result_1)

# # graph_points_2 = ['P1', 'Q1', 'P2']
# # middle_points_2 = ['R1', 'R2']
# # result_2 = gather_graph_points(graph_points_2, middle_points_2)
# # print(result_2)

# # graph_points_3 = ['P1', 'R1', 'Q1', 'R2', 'P2']
# # middle_points_3 = ['S1', 'S2', 'S3', 'S4']
# # result_3 = gather_graph_points(graph_points_3, middle_points_3)
# # print(result_3)



# # def recursive_segmentation(points, length):
# #     num_points = len(points)
# #     if num_points <= length:
# #         return [points]
# #     else:
# #         midpoint = num_points // 2
# #         left_half = points[:midpoint+1]
# #         right_half = points[midpoint:]
# #         return recursive_segmentation(left_half, length) + recursive_segmentation(right_half, length)

# # # Test the function
# # points = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10', 'P11', 'P12', 'P13','P14'
# # ,'P15'
# # ,'P16'
# # ,'P17'
# # ,'P18'
# # ,'P19'
# # ,'P20'
# # ,'P21'
# # ,'P22'
# # ,'P23'
# # ,'P24'
# # ,'P25']
# # segmented_points = recursive_segmentation(points, 4)

# # print("Segmented Points:")
# # for segment in segmented_points:
# #     print(segment)

# # def split_into_segments(points, segment_length):
# #     num_segments = len(points) - segment_length + 1
# #     segments = [points[i:i+segment_length] for i in range(num_segments)]
# #     return segments

# # # Test the function
# # points = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10', 'P11', 'P12', 'P13', ]
# # segment_length = 4
# # segmented_points = split_into_segments(points, segment_length)

# # print("Segmented Points:")
# # for segment in segmented_points:
# #     print(segment)

# # def divide_points(points, next_points, iteration):
# #     divided_points = []
# #     length = len(points)


# #     div = len(next_points) // 2
# #     process1 = next_points[:div + 1]
# #     process2 = next_points[div:]

# #     if len(process2) > length and len(process2) == len(process1):
# #         div = len(process2) // 2
# #         process11 = process1[:div + 1]
# #         process12 = process1[div:]
# #         divided_points.append(process11)
# #         divided_points.append(process12)
# #         div = len(process2) // 2
# #         process21 = process2[:div + 1]
# #         process22 = process2[div:]
# #         divided_points.append(process21)
# #         divided_points.append(process22)
# #     else:
# #         divided_points.append(process1)
# #         divided_points.append(process2)

# #     return divide_points



# # # Test the function
# # points = ['1', '2', '3', '4']
# # next_points = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10', 'P11', 'P12', 'P13']
# # divided_points = divide_points(points, next_points, 4)

# # print("Divided Points:")
# # for part in divided_points:
# #     print(part)


#     # points_per_part = num_total_points // num_parts
    
#     # for i in range(num_parts):
#     #     start_index = i * points_per_part
#     #     end_index = start_index + points_per_part
        
#     #     # Handle the last part if it doesn't evenly divide the points
#     #     if i == num_parts - 1:
#     #         end_index = num_total_points
        
#     #     divided_points.append(points[start_index:end_index])

# # ,'P14'
# # ,'P15'
# # ,'P16'
# # ,'P17'
# # ,'P18'
# # ,'P19'
# # ,'P20'
# # ,'P21'
# # ,'P22'
# # ,'P23'
# # ,'P24'
# # ,'P25'
    
# # def next_iteration(next_points, graph_points):
    
# #     div = len(next_points) // 2
# #     print(div)
# #     process1 = next_points[:div + 1]
# #     process2 = next_points[div:]
# #     print("first: " ,process1)
# #     print("second: " ,process2)
# #     first_half = [process1[0], process1[-1]]
# #     second_half = [process2[0], process2[-1]]
# #     first_to_graph, first_half = recursive_midpoint(process1, first_half)
# #     print("\nfirst midpoint: " ,first_to_graph)
# #     print("\nfirst next_point: " ,first_half)
# #     second_to_graph, second_half = recursive_midpoint(process2, second_half)
# #     print("\nsecond midpoint: " , second_to_graph)
# #     print("\nsecond next_point: " , second_half)
# #     to1 = len(graph_points) // 2
# #     graph_points.insert(to1, first_to_graph)
# #     to2 = (len(graph_points) // 2) + 1
# #     graph_points.insert(to2, second_to_graph)
# #     print("\nto graph: " , graph_points)
# #     new_next_points = first_half[:-1] + second_half
# #     print("\nnew: " , new_next_points)
# #     print("\npanjang new: " , len(new_next_points))
# #     return new_next_points, graph_points
    
