def console_and_move():

    while True:
        n = input('������� �������� ��������� ��������� (h - �������) > ')

        if n == 'h':
            print('\n�������:')
            print('     ����� - ����� ��������� �� ��������� ���������� (� ��)')
            print('     s - �������� ������� ��������� ���������')
            print('     z - ���������� ��������� �� 0')
            print('     q - �����')
            print('Try in now!\n')

        elif n == 's':
            print(round(steps / k_move), ' ��')

        elif n == 'z':
            stepBackward(abs(steps))
            steps = 0
            print(round(steps / k_move), ' ��')

        elif n == 'q':
            stepBackward(abs(steps))
            exit

        else:
            n = int(n)
            if (n in (0, 100)):
                if n * k_move < steps:
                    
                    stepBackward(abs(n * k_move - steps))
                if n * k_move > steps:
                    stepForward(n * k_move - steps)
                                    

                steps += n * k_move
            else:
                print('���������� �����/n')