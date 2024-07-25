#version 330 core

layout(location = 0) in vec3 in_position;
layout(location = 1) in vec3 in_normal;

out vec3 color;

void main() {
    color = in_normal;
    gl_Position = vec4(in_position, 1.0);
}
