def flood_fill(image, sr, sc, color):
    if not image or not image[0]:
        return image

    original_color = image[sr][sc]
    if original_color == color:
        return image

    rows = len(image)
    cols = len(image[0])
    stack = [(sr,sc)]
    image[sr][sc] = color

    while stack:
        row, col = stack.pop()
        
        for new_row, new_col in (
            (row+1, col),
        (row-1, col),
        (row, col+1),
        (row, col-1),
        ):
            if(
                0 <= new_row < rows and
                0 <= new_col < cols and
                image[new_row][new_col] == original_color
            ):
                image[new_row][new_col] = color
                stack.append((new_row, new_col))
    return image


if __name__ == "__main__":
    sr = int(input())
    sc = int(input())
    color = int(input())

    m, n = list(map(int, input().split(' ')))

    image = [list(map(int, input().split(' '))) for _ in range(m)]

    print(
        flood_fill(image, sr, sc, color)
    )


