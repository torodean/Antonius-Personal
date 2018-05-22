#include "wizardui.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    WizardUI w;
    w.show();

    return a.exec();
}
