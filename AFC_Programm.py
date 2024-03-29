from Devices.AD9833 import *
from Controller import *
from Devices.AD7606 import Ad7606
from Devices.AD8400 import AD8400
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import time
f_start = 7000  #начальная частота
f_stop = 9000   #конечная частота
f_step = 10      #шаг частоты при измерении
gain = 250      #установка усиления

plot = 1        #строить график
repeat = True      #повтор измерений в одной точке
median = 0      #применение медианного фильтра

rep_num = 5     #кол-во повторов в одной точке
adc_channel = 2 #канал АЦП

if __name__ == '__main__':
    serialWriterReader.clean()
    controller.addDeviceToPort(WaveGen(AD9833_SPI_PORT))
    controller.addDeviceToPort(Ad7606(AD7606_SPI_PORT))
    controller.get(AD7606_SPI_PORT).reboot()
    controller.addDeviceToPort(AD8400(DAC8563_1_SPI_PORT))

    controller.get(DAC8563_1_SPI_PORT).setGain(gain)
    controller.get(AD9833_SPI_PORT).send_f(f_start)
    common_data = controller.get(AD7606_SPI_PORT).read().split(',')

    time.sleep(0.5)

    while len(common_data) != 4:
        common_data = controller.get(AD7606_SPI_PORT).read().split(',')

    a = int(common_data[adc_channel])
    b = a
    c = a

    current_datetime = datetime.now()
    print(a)
    print("Current date & time : ", current_datetime)
    str_current_datetime = str(current_datetime)
    str_current_datetime = str_current_datetime[:-7]
    str_current_datetime = str_current_datetime.replace(':', '-')
    file_name = str_current_datetime + '.txt'
    afc_name = str_current_datetime + '.png'
    datafile = open("Logs/" + file_name, 'a+')

    for m in range(f_start, f_stop, f_step):
        values = []
        # controller.get(AD9833_SPI_PORT).send_f(m)
        # datafile = open("Logs/" + file_name, 'a+')
        if repeat:
            point_sum = 0
            for i in range(0, rep_num, 1):
                controller.get(AD9833_SPI_PORT).send_freq(m)
                time.sleep(0.01)
                common_data = controller.get(AD7606_SPI_PORT).read().split(',')
                while len(common_data) != 4:
                    common_data = controller.get(AD7606_SPI_PORT).read().split(',')
                point_sum += int(common_data[adc_channel])
            amplitude = point_sum / rep_num
            if amplitude > 32767:
                amplitude = amplitude - 65536

        else:
            controller.get(AD9833_SPI_PORT).send_freq(m)
            time.sleep(0.005)
            common_data = controller.get(AD7606_SPI_PORT).read().split()
            if len(common_data) == 0:
                continue
            amplitude = int(common_data[adc_channel])

        # if median:
        #     c = b
        #     b = a
        #     a = amplitude
        #     amplitude_data = max(a, c) if (max(a, b) == max(b, c)) else max(b, min(a, c))
        # else:
        #     amplitude_data = amplitude

        c = b
        b = a
        a = amplitude
        amplitude_meddle = max(a, c) if (max(a, b) == max(b, c)) else max(b, min(a, c))


        datafile.write(str(m) + ' ' + str(amplitude) + ' ' + str(amplitude_meddle) + "\n")


    datafile.close()
    # exit(0)
    if plot:
        datafile = open("Logs/" + file_name, 'a+')
        datafile.write("START " + str(f_start) + "\n" + "STOP " + str(f_stop) + "\n" + "STEP " + str(f_step) + "\n")
        data2 = np.loadtxt("Logs/" + file_name)
        x = data2[:, 0]
        y = data2[:, 1]
        z = data2[:, 2]
        plt.plot(x, y, 'r:')
        plt.plot(x, z, 'g--')
        plt.title('Резонанс датчика')
        plt.xlabel('Частота, КГц')
        plt.ylabel('Амплитуда')
        plt.grid(1, 'both', 'both')
        plt.axis([f_start, f_stop, round(min(y), -4)-5000, round(max(y), -4)+5000])
        plt.savefig("Logs/" + afc_name, dpi=300)
    datafile.close()
    plt.show()
    print("finish")
    plt.draw()