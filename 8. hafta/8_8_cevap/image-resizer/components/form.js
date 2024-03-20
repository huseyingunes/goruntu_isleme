"use client"

import { UploadImageAction } from "@/image-upload"
import { useFormState } from "react-dom"

const initialState = {
    path: "bugday-1710328648358-489962882.jpeg"
}

export default function Form() {

    const [state, formAction] = useFormState(UploadImageAction, initialState)

    return <form className="max-w-screen-xl mx-auto flex flex-col md:flex-row min-h-screen w-full" action={formAction}>
        <div className="container flex flex-col items-center justify-center w-full m-5">
            <div className="flex flex-col w-full gap-10">
                <label className="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 dark:hover:bg-bray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600">
                    <div className="flex flex-col items-center justify-center pt-5 pb-6">
                        <svg
                            className="w-10 h-10 mb-3 text-gray-400"
                            fill="none"
                            stroke="currentColor"
                            viewBox="0 0 24 24"
                            xmlns="http://www.w3.org/2000/svg"
                        >
                            <path
                                strokeLinecap="round"
                                strokeLinejoin="round"
                                strokeWidth="2"
                                d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
                            ></path>
                        </svg>
                        <p className="mb-2 text-sm text-gray-500 dark:text-gray-400">
                            <span className="font-semibold">
                                Click to upload
                            </span>{' '}
                            or drag and drop
                        </p>
                        <p className="text-xs text-gray-500 dark:text-gray-400">
                            SVG, PNG, JPG or GIF
                        </p>
                    </div>
                    <input
                        id="file"
                        name="file"
                        type="file"
                        className="hidden"
                        accept="image/png image/jpg image/jpeg"
                    />
                </label>

                <label htmlFor="heigth" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Heigth:</label>
                <input type="number" id="heigth" name="heigth" aria-describedby="helper-text-explanation" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="90210" required />

                <label htmlFor="width" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Width:</label>
                <input type="number" id="width" name="width" aria-describedby="helper-text-explanation" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="90210" required />

                <button type="submit" className="px-4 py-2 bg-green-400">Submit</button>
            </div>

            <img
                src={state.path}
                className="mt-10"
            />
        </div>

    </form>

}