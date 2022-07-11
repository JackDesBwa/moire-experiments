import QtQuick 2.0

Rectangle {
    width: src1.width
    height: src1.height
    color: '#1e1e1e'

    ShaderEffectSource {
        id: src1
        width: sourceItem.width; height: sourceItem.height
        sourceItem: Image {
            source: "/tmp/i1.png"
        }
    }
    ShaderEffectSource {
        id: src2
        width: sourceItem.width; height: sourceItem.height
        sourceItem: Item {
            width: img2.width
            height: img2.height
            Image {
                id: img2
                source: "/tmp/i2.png"
                x: shader.dx
                y: shader.dy
                rotation: shader.angle
            }
        }
    }
    ShaderEffect {
        id: shader
        width: parent.width; height: parent.height

        property variant source1: src1
        property variant source2: src2

        property real x0: 0
        property real y0: 0
        property real dx0: 0
        property real dy0: 0
        property real dx: 0
        property real dy: 0
        property real angle: 0

        MouseArea {
            anchors.fill: parent
            acceptedButtons: Qt.LeftButton | Qt.RightButton
            onPressed: {
                parent.x0 = mouse.x
                parent.y0 = mouse.y
                parent.dx0 = parent.dx
                parent.dy0 = parent.dy
            }
            onPositionChanged: {
                if (pressedButtons & Qt.LeftButton) {
                    if (mouse.modifiers & Qt.AltModifier) {
                        parent.angle = Math.atan2(mouse.y-height/2, mouse.x-width/2)*180/Math.PI;
                    } else {
                        if (!(mouse.modifiers & Qt.ShiftModifier))
                            parent.dx = parent.dx0 + (mouse.x - parent.x0);
                        if (!(mouse.modifiers & Qt.ControlModifier))
                            parent.dy = parent.dy0 + (mouse.y - parent.y0);
                    }
                } else {
                    parent.angle = Math.atan2(mouse.y-height/2, mouse.x-width/2)*180/Math.PI;
                }
            }
            onDoubleClicked: {
                if (pressedButtons & Qt.LeftButton) {
                    parent.dx = 0;
                    parent.dy = 0;
                } else {
                    parent.angle = 0;
                }
            }
        }

        fragmentShader: "
                varying highp vec2 qt_TexCoord0;

                uniform sampler2D source1;
                uniform sampler2D source2;

                void main() {
                    gl_FragColor = texture2D(source1, qt_TexCoord0) * texture2D(source2, qt_TexCoord0);
                }"
    }

}
