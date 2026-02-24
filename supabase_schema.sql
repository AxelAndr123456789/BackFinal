-- HealthConnect Database Schema for Supabase

-- Tablas
CREATE TABLE IF NOT EXISTS especialidades (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    icono VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    telefono VARCHAR(50),
    fecha_nacimiento DATE,
    genero VARCHAR(50),
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS doctores (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    especialidad_id INTEGER REFERENCES especialidades(id) ON DELETE CASCADE,
    licencia VARCHAR(100) UNIQUE NOT NULL,
    biografia TEXT,
    foto_url TEXT,
    anos_experiencia INTEGER,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS disponibilidad (
    id SERIAL PRIMARY KEY,
    doctor_id INTEGER REFERENCES doctores(id) ON DELETE CASCADE,
    fecha DATE NOT NULL,
    hora_inicio TIME NOT NULL,
    hora_fin TIME NOT NULL,
    esta_disponible BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS citas (
    id SERIAL PRIMARY KEY,
    usuario_id INTEGER REFERENCES usuarios(id) ON DELETE CASCADE,
    doctor_id INTEGER REFERENCES doctores(id) ON DELETE CASCADE,
    especialidad_id INTEGER REFERENCES especialidades(id) ON DELETE CASCADE,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    motivo TEXT,
    notas TEXT,
    estado VARCHAR(50) DEFAULT 'programada',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Índices
CREATE INDEX IF NOT EXISTS idx_doctores_especialidad ON doctores(especialidad_id);
CREATE INDEX IF NOT EXISTS idx_disponibilidad_doctor ON disponibilidad(doctor_id);
CREATE INDEX IF NOT EXISTS idx_disponibilidad_fecha ON disponibilidad(fecha);
CREATE INDEX IF NOT EXISTS idx_citas_usuario ON citas(usuario_id);
CREATE INDEX IF NOT EXISTS idx_citas_doctor ON citas(doctor_id);
CREATE INDEX IF NOT EXISTS idx_citas_fecha ON citas(fecha);
CREATE INDEX IF NOT EXISTS idx_citas_estado ON citas(estado);

-- Especialidades
INSERT INTO especialidades (nombre, descripcion, icono) VALUES
    ('Cardiología', 'Enfermedades del corazón', 'heart'),
    ('Dermatología', 'Enfermedades de la piel', 'skin'),
    ('Pediatría', 'Atención a niños', 'child'),
    ('Ginecología', 'Salud femenina', 'woman'),
    ('Oftalmología', 'Enfermedades de los ojos', 'eye'),
    ('Ortopedia', 'Sistema musculoesquelético', 'bone'),
    ('Neurología', 'Sistema nervioso', 'brain'),
    ('Medicina General', 'Atención primaria', 'general');

-- Usuarios
INSERT INTO usuarios (email, nombre, apellido, telefono, fecha_nacimiento, genero, password) VALUES
    ('juan.perez@email.com', 'Juan', 'Pérez', '+52 555 123 4567', '1990-05-15', 'Masculino', 'password123'),
    ('maria.garcia@email.com', 'María', 'García', '+52 555 234 5678', '1985-08-22', 'Femenino', 'password123'),
    ('carlos.lopez@email.com', 'Carlos', 'López', '+52 555 345 6789', '1992-03-10', 'Masculino', 'password123'),
    ('ana.rodriguez@email.com', 'Ana', 'Rodríguez', '+52 555 456 7890', '1988-12-05', 'Femenino', 'password123'),
    ('test@healthconnect.com', 'Usuario', 'Test', '+52 555 999 9999', '1995-01-01', 'Masculino', 'test123');

-- Doctores
INSERT INTO doctores (nombre, apellido, especialidad_id, licencia, biografia, anos_experiencia) VALUES
    ('Juan', 'Pérez', 1, 'LM-001', 'Cardiólogo con 15 años de experiencia', 15),
    ('María', 'García', 2, 'LM-002', 'Dermatóloga especialista en piel', 10),
    ('Carlos', 'López', 3, 'LM-003', 'Pediatra con atención especial a niños', 8),
    ('Ana', 'Rodríguez', 4, 'LM-004', 'Ginecóloga certificada', 12),
    ('Roberto', 'Martínez', 1, 'LM-005', 'Especialista en cirugía cardíaca', 20),
    ('Laura', 'Sánchez', 5, 'LM-006', 'Oftalmóloga especialista en retina', 7),
    ('Fernando', 'Torres', 6, 'LM-007', 'Ortopedista deportiva', 12),
    ('Patricia', 'Jiménez', 7, 'LM-008', 'Neuróloga clínica', 9);

-- Disponibilidad
INSERT INTO disponibilidad (doctor_id, fecha, hora_inicio, hora_fin, esta_disponible) VALUES
    (1, '2026-02-10', '08:00:00', '12:00:00', TRUE),
    (1, '2026-02-10', '14:00:00', '17:00:00', TRUE),
    (1, '2026-02-12', '08:00:00', '12:00:00', TRUE),
    (1, '2026-02-12', '14:00:00', '17:00:00', TRUE),
    (1, '2026-02-15', '08:00:00', '12:00:00', TRUE),
    (1, '2026-02-15', '14:00:00', '17:00:00', TRUE),
    (1, '2026-02-18', '08:00:00', '12:00:00', TRUE),
    (1, '2026-02-18', '14:00:00', '17:00:00', TRUE),
    (1, '2026-02-20', '08:00:00', '12:00:00', TRUE),
    (1, '2026-02-20', '14:00:00', '17:00:00', TRUE),
    (1, '2026-02-22', '08:00:00', '12:00:00', TRUE),
    (1, '2026-02-22', '14:00:00', '17:00:00', TRUE),
    (2, '2026-02-11', '09:00:00', '13:00:00', TRUE),
    (2, '2026-02-11', '15:00:00', '18:00:00', TRUE),
    (2, '2026-02-13', '09:00:00', '13:00:00', TRUE),
    (2, '2026-02-13', '15:00:00', '18:00:00', TRUE),
    (2, '2026-02-16', '09:00:00', '13:00:00', TRUE),
    (2, '2026-02-16', '15:00:00', '18:00:00', TRUE),
    (2, '2026-02-19', '09:00:00', '13:00:00', TRUE),
    (2, '2026-02-19', '15:00:00', '18:00:00', TRUE),
    (3, '2026-02-10', '08:30:00', '12:30:00', TRUE),
    (3, '2026-02-10', '14:30:00', '17:30:00', TRUE),
    (3, '2026-02-14', '08:30:00', '12:30:00', TRUE),
    (3, '2026-02-14', '14:30:00', '17:30:00', TRUE),
    (3, '2026-02-17', '08:30:00', '12:30:00', TRUE),
    (3, '2026-02-17', '14:30:00', '17:30:00', TRUE),
    (3, '2026-02-21', '08:30:00', '12:30:00', TRUE),
    (3, '2026-02-21', '14:30:00', '17:30:00', TRUE);

-- Citas
INSERT INTO citas (usuario_id, doctor_id, especialidad_id, fecha, hora, motivo, estado) VALUES
    (1, 1, 1, '2026-02-25', '09:00:00', 'Chequeo cardiológico anual', 'programada'),
    (2, 2, 2, '2026-02-26', '10:30:00', 'Revisión de manchas en la piel', 'programada'),
    (3, 3, 3, '2026-02-27', '11:00:00', 'Vacunación del niño', 'programada'),
    (4, 4, 4, '2026-02-28', '09:30:00', 'Control prenatal', 'programada'),
    (1, 3, 3, '2026-01-15', '08:00:00', 'Consulta general', 'completada'),
    (2, 1, 1, '2026-01-20', '14:00:00', 'Dolor en el pecho', 'completada'),
    (5, 2, 2, '2026-01-25', '11:00:00', 'Dermatitis', 'completada'),
    (3, 1, 1, '2026-02-05', '10:00:00', 'Chequeo preventivo', 'cancelada'),
    (4, 3, 3, '2026-02-10', '15:00:00', 'Enfermedad viral', 'cancelada');
