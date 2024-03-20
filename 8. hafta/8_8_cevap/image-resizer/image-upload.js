'use server';

import { exec } from 'child_process';
import mime from "mime";
import { join } from "path";
import { stat, mkdir, writeFile } from "fs/promises";

export async function UploadImageAction(prevState, formData) {
    const file = formData.get("file")
    const buffer = Buffer.from(await file.arrayBuffer());
    const relativeUploadDir = `pic`;
    const uploadDir = join(process.cwd(), "public", relativeUploadDir);

    try {
        await stat(uploadDir);
    } catch (e) {
        if (e.code === "ENOENT") {
            await mkdir(uploadDir, { recursive: true });
        } else {
            console.error(
                "Error while trying to create directory when uploading a file\n",
                e
            );
            return NextResponse.json({ success: false });
        }
    }

    const uniqueSuffix = `${Date.now()}-${Math.round(Math.random() * 1e9)}`;
    const filename = `${file.name.replace(
        /\.[^/.]+$/,
        ""
    )}-${uniqueSuffix}.${mime.getExtension(file.type)}`.replace(" ", "");
    await writeFile(`${uploadDir}/${filename}`, buffer);

    const fileUrl = `${relativeUploadDir}/${filename}`;

    const pythonKomutu = `python script.py ${fileUrl} ${filename} ${formData.get("heigth")} ${formData.get("width")}`;

    let new_path = "";

    const { stdout, stderr } = await new Promise((resolve, reject) => {
        exec(pythonKomutu, (error, stdout, stderr) => {
            if (error) {
                console.error(`Hata oluştu: ${error}`);
                reject(error);
            } else {
                resolve({ stdout, stderr });
            }
        });
    });

    if (stdout) {
        console.log(`Çıktı: ${stdout}`);
        new_path = stdout.trim();
    } else {
        console.error(`Hata çıktısı: ${stderr}`);
    }

    return {
        path: new_path
    }
}
